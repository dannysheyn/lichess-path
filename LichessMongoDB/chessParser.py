import chess
import chess.pgn


class chess_pgn_parser:
    def __init__(self, data_file_path):
        data_file = open(data_file_path)
        self.pgn_file_path = data_file.readline()
        self.games_parsed = int(data_file.readline())
        data_file.close()
        return

    def parse_chess_db(self):
        chess_db_file = open(self.pgn_file_path)
        # pgn_file_not_ended = False
        for i in range(10):
            header = chess.pgn.read_headers(chess_db_file)
        return

    def save_number_of_iterations(self):
        file = open("num_of_iterations.txt", "w")
        file.write(str(self.games_parsed))
        file.close()
        return
