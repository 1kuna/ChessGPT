import tkinter as tk
import chess
import chess.engine
import time
import threading

engine = chess.engine.SimpleEngine.popen_uci("stockfish\\engine.exe")

# Create a new window
window = tk.Tk()

# Set the window title
window.title("Chess")

# Create a new canvas
canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()

# Draw the chess board
def draw_board():
    for row in range(8):
        for col in range(8):
            color = "white" if (row + col) % 2 == 0 else "gray"
            canvas.create_rectangle(col * 50, row * 50, (col + 1) * 50, (row + 1) * 50, fill=color)
    window.update_idletasks()

# Draw the chess pieces
piece_images = {
    "P": tk.PhotoImage(file="pieces\\wp.png"),
    "N": tk.PhotoImage(file="pieces\\wn.png"),
    "B": tk.PhotoImage(file="pieces\\wb.png"),
    "R": tk.PhotoImage(file="pieces\\wr.png"),
    "Q": tk.PhotoImage(file="pieces\\wq.png"),
    "K": tk.PhotoImage(file="pieces\\wk.png"),
    "p": tk.PhotoImage(file="pieces\\bp.png"),
    "n": tk.PhotoImage(file="pieces\\bn.png"),
    "b": tk.PhotoImage(file="pieces\\bb.png"),
    "r": tk.PhotoImage(file="pieces\\br.png"),
    "q": tk.PhotoImage(file="pieces\\bq.png"),
    "k": tk.PhotoImage(file="pieces\\bk.png"),
}
def draw_pieces(board):
    canvas.delete("piece")
    for row in range(8):
        for col in range(8):
            square = chess.square(col, 7 - row)
            piece = board.piece_at(square)
            if piece is not None:
                image = piece_images[piece.symbol()]
                canvas.create_image(col * 50 + 25, row * 50 + 25, image=image, tags=("piece",))
    window.update_idletasks()

# Create the Text widget
moves_text = tk.Text(window, height=24, width=20)
moves_text.place(x=420)

# Define the game loop
def game_loop():
    board = chess.Board()
    move_num = 1
    while not board.is_game_over():
        draw_board()
        draw_pieces(board)
        time.sleep(1)
        window.update()
        result = engine.play(board, chess.engine.Limit(time=0.5))
        if result.move is not None:
            # Get the player who made the move
            player = "White" if board.turn == chess.WHITE else "Black"
            # Append the move to the Text widget
            move_str = f"{move_num}. {player}: {result.move.uci()}\n"
            moves_text.insert("end", move_str)
            # Scroll the Text widget down
            moves_text.yview_moveto(1.0)
            # Increment the move number
            move_num += 1
            board.push(result.move)

    # Draw the final board
    draw_board()
    draw_pieces(board)
    window.update()

    # Stop the engine
    engine.quit()

# Define the function to handle the WM_DELETE_WINDOW protocol
def on_closing():
    engine.quit()
    window.destroy()

# Bind the WM_DELETE_WINDOW protocol to the window
window.protocol("WM_DELETE_WINDOW", on_closing)

# Start the game loop in a new thread
thread = threading.Thread(target=game_loop)
thread.start()

# Start the main event loop
window.mainloop()