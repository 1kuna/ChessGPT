import chess.engine
import chess.pgn
import io

def parse_pgn():
    game_path = input("Enter either the PGN code or file path: ")
    if game_path.endswith(".pgn"):
        with open(game_path) as pgn_file:
            game = chess.pgn.read_game(pgn_file)
    else:
        game = chess.pgn.read_game(io.StringIO(game_path))
    return game


def get_best_move():
    # Start the Stockfish engine
    engine = chess.engine.SimpleEngine.popen_uci("stockfish\\engine.exe")

    # Set the board to the starting position
    board = chess.Board()

    # Get the best move for the current position
    result = engine.play(board, chess.engine.Limit(time=2.0))
    best_move = result.move

    # Stop the engine
    engine.quit()

    return best_move