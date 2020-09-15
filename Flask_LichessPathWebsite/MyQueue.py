import queue
from collections import deque


class myQueue:
    def __init__(self):
        self.queue = deque()
        self.name_set = set()

    def Enqueue(self, userVertex):
        if self.name_set.__contains__(userVertex.user['User_Name']):
            return
        else:
            self.queue.append(userVertex)
            self.name_set.add(userVertex.user['User_Name'])

    def IsEmpty(self):
        return self.queue.__len__() == 0

    def Dequeue(self):
        return self.queue.popleft()

    def Contains(self, user):
        return self.name_set.__contains__(user['User_Name'])

    def InsertFirst(self, userVertex):
        self.queue.appendleft(userVertex)

    def Clear(self):
        self.queue.clear()
        self.name_set.clear()
        return
