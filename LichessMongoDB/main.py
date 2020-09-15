import pymongo
import UserDBController
import chessParser
import chess.pgn
import queue

# client = pymongo.MongoClient(
#    "mongodb+srv://Dadmin:4yjqRA9z7CduBMD@cluster0.miqhi.mongodb.net/<dbname>?retryWrites=true&w=majority")
# db = client['LichessPlayerGraph']
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
client = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
current_doc_limit = 1000000

q = queue.Queue()

if __name__ == '__main__':
    user_db = UserDBController.UserDB(client, 'LichessDB', 'PlayerGraph')
    pgn_parser = chessParser.chess_pgn_parser('ChessData.txt')
    chess_db_file = open(pgn_parser.pgn_file_path[:-1])
    num_of_documents = user_db.get_number_of_documents()
    while num_of_documents < current_doc_limit:
        try:
            header = chess.pgn.read_headers(chess_db_file)
            user_db.insert_won_user(header['White'], header['Black'], header['Result'])
            pgn_parser.games_parsed += 1
            num_of_documents = user_db.get_number_of_documents()
            if pgn_parser.games_parsed % 100000 == 0:
                print("100,000 iterations have passed")
            if num_of_documents % 10000 == 0:
                print("number of documents : " + str(num_of_documents))
        except Exception as inst:
            print("Exception raised as: white" + str(header['White']) + " black: " + str(header['Black']))
            print(inst)
    pgn_parser.save_number_of_iterations()
