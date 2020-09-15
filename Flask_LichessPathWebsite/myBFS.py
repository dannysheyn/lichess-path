from MyQueue import myQueue
from UserVertex import UserVertex
import pymongo


def parent_path(user_path: UserVertex):
    returned_string = ''
    lt = [user_path.Name]
    degree_count = 0
    while user_path.parent is not None:
        user_path = user_path.parent
        lt.append(' -> ')
        lt.append(user_path.Name)
        degree_count += 1
    lt.reverse()
    for i in lt:
        returned_string += i
    returned_string += ' you are {} degrees from magnus!'.format(degree_count)
    return returned_string


class FindRouteToMagnus():
    def __init__(self, client, db_name, collection_name):
        self.client = client
        self.db = client[db_name]
        self.db_collection = self.db.get_collection(collection_name)
        self.queue = myQueue()

    def find_path_to_magnus(self, user_name):
        user_in_db = self.db_collection.find_one({'User_Name': user_name})
        current_user_vertex = UserVertex(user_in_db, None, 0)  # parent =none , distance = 0
        returned_string = 'Sorry, no path from you to magnus'
        if user_in_db is None:
            return returned_string
        self.queue.Enqueue(current_user_vertex)
        while not self.queue.IsEmpty():
            current_user = self.queue.Dequeue()
            if current_user.user['User_Name'] == 'DrNykterstein':
                self.queue.Clear()
                return parent_path(current_user)
            won_list = current_user.WonList
            if 'DrNykterstein' in won_list:
                self.queue.InsertFirst(UserVertex(self.db_collection.find_one({'User_Name': 'DrNykterstein'}),
                                                  current_user, current_user.distance + 1))
            else:
                user_won_dict = self.db_collection.find_one({'User_Name': {'$in': won_list}},
                                                            sort=[('Distance', pymongo.ASCENDING)])
                self.check_name_and_insert_queue(current_user, user_won_dict)
        self.queue.Clear()
        return returned_string

    def check_name_and_insert_queue(self, current_user, won_user):
        if self.queue.name_set.__contains__(won_user['User_Name']):
            pass
        else:
            neighbor_vertex = UserVertex(won_user,
                                         current_user, current_user.distance + 1)
            self.queue.Enqueue(neighbor_vertex)
