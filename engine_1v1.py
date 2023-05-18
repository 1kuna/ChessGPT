import chess
import chess.engine
import time
import threading
import chessboard_ui as cb

engine = chess.engine.SimpleEngine.popen_uci("stockfish\\engine.exe")

# Define the game loop
def game_loop():
    board = chess.Board()
    move_num = 1
    while not board.is_game_over():
        cb.draw_board()
        cb.draw_pieces(board)
        time.sleep(1)
        cb.window.update()
        result = engine.play(board, chess.engine.Limit(time=0.5))
        if result.move is not None:
            # Get the player who made the move
            player = "White" if board.turn == chess.WHITE else "Black"
            # Append the move to the Text widget
            move_str = f"{move_num}. {player}: {result.move.uci()}\n"
            cb.moves_text.insert("end", move_str)
            # Scroll the Text widget down
            cb.moves_text.yview_moveto(1.0)
            # Increment the move number
            move_num += 1
            board.push(result.move)

    # Draw the final board
    cb.draw_board()
    cb.draw_pieces(board)
    cb.window.update()

    # Stop the engine
    engine.quit()

# Define the function to handle the WM_DELETE_WINDOW protocol
def on_closing():
    engine.quit()
    cb.window.destroy()

# Bind the WM_DELETE_WINDOW protocol to the window
cb.window.protocol("WM_DELETE_WINDOW", on_closing)

# Start the game loop in a new thread
thread = threading.Thread(target=game_loop)
thread.start()

# Start the main event loop
cb.window.mainloop()