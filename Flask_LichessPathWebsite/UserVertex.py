class UserVertex:
    def __init__(self, user, parent, distance):
        self.user = user
        self.parent = parent
        self.distance = distance

    @property
    def Name(self):
        return self.user['User_Name']

    @property
    def WonList(self):
        return self.user['Users_Won']
