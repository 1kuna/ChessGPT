import chess.engine
import chess.pgn
import io
import chessboard_ui as cb

# TODO: Create a unit test for each function
# TODO: Incorporate chessboard (player and engine) moves text UI 

def parse_pgn():
    game_path = input("Enter either the PGN code or file path: ")
    if game_path.endswith(".pgn"):
        game = chess.pgn.read_game(open(game_path))
    else:
        game = chess.pgn.read_game(io.StringIO(game_path))

    if game is None:
        print("Invalid PGN code or file path")
        return None
    
    return game

def get_best_move(game):
    # Set the board to the starting position
    board = game.board()

    # Start the Stockfish engine
    engine = chess.engine.SimpleEngine.popen_uci("stockfish\\engine.exe")

    # Loop through each move in the game
    for move in game.mainline_moves():
        # Make the move on the board
        board.push(move)

        # Get the best move for the current position
        result = engine.play(board, chess.engine.Limit(time=2.0))
        best_move = result.move

        # Print the best move for the current position
        if best_move == None:
            print("Game over!")
        else:
            print(f"Best move for position after {board.move_stack[-1]}: {best_move}")

    # Stop the engine
    engine.quit()

    # Print the final board
    print(board)

    # Print the game result
    print(game.headers["White"], "vs.", game.headers["Black"], "\n", game.headers["Result"])

    return game

game = parse_pgn()
get_best_move(game)