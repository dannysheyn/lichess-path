import json
import pymongo
from pymongo import MongoClient
import users


class UserDB:
    def __init__(self, client, db_name, collection_name):
        self.client = client
        self.db = client[db_name]
        self.db_collection = self.db.get_collection(collection_name)

    def insert_won_user(self, white_name, black_name, result):
        white_won = '1-0'
        black_won = '0-1'
        if result == white_won:
            self.push_user(white_name, black_name)
        else:
            self.push_user(black_name, white_name)
        return

    def push_user(self, user_name, lost_user_name):
        users_won_key = 'Users_Won'
        filter_key = '_id'
        update_key = '$addToSet'

        found_user = self.find_user_by_parameter(parameter="User_Name", user_query=user_name)
        if found_user == None:
            found_user = users.User(user_name)
            found_user.add_won_user(lost_user_name)
            self.db_collection.insert_one((found_user.to_json()))
        else:
            user_id = found_user['_id']
            self.db_collection.find_one_and_update({filter_key: user_id}, {update_key: {users_won_key: lost_user_name}})
            self.update_users_won_count(found_user, user_id, lost_user_name)
        return

    def update_users_won_count(self, found_user, user_id, lost_user_name):
        users_won_count_key = 'Users_Won_Count'
        filter_key = '_id'
        inc_key = '$inc'
        if not found_user['Users_Won'].__contains__(lost_user_name):
            self.db_collection.find_one_and_update({filter_key: user_id}, {inc_key: {users_won_count_key: 1}})
        return

    def find_user_by_parameter(self, parameter, user_query):
        return self.db_collection.find_one({parameter: user_query})

    def get_number_of_documents(self):
        return self.db_collection.estimated_document_count()
