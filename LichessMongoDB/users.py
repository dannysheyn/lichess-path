import json


class User:
    def __init__(self, user_name):
        self.User_Name = user_name
        self.Users_Won = set()
        self.Users_Won_Count = len(self.Users_Won)

    def to_json(self):
        return json.loads(json.dumps(self.__dict__, default=set_to_list))

    def add_won_user(self, obj):
        self.Users_Won.add(obj)
        self.Users_Won_Count = len(self.Users_Won)
        return


def set_to_list(self):
    return list(self)
