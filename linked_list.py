from node import *

class LinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None
        self.length = 0

    def __str__(self):
        if self.begin is not None:
            current = self.begin
            out = 'LinkedList [' + str(current.value)
            while current.next is not None:
                current = current.next
                out += ', ' + str(current.value)
            return out + ']'
        else:
            return 'LinkedList[]'

    def clear(self):
        self.__init__()

    def push(self, arg):
        if self.begin is None:
            self.end = self.begin = Node(arg, None)
        else:
            self.begin = Node(arg, self.begin)

    def add(self, arg):
        if self.begin is None:
            self.end = self.begin = Node(arg, None)
        else:
            self.end.next = self.end = Node(arg, None)

    def insert(self, arg, index):
        if self.begin is None:
            self.begin = Node(arg, self.begin)
            self.end = self.begin.next
            return
        if index == 0:
            self.begin = Node(arg, self.begin)
            return
        current = self.begin
        count = 0
        while current is not None:
            count += 1
            if count == index:
                current.next = Node(arg, current.next)
                if current.next.next is None:
                    self.end = current.next
                break
            current = current.next

    def list_length(self):
        length = 0
        if self.begin is not None:
            current = self.begin
            while current.next is not None:
                length += 1
                current = current.next
            return length + 1
        else:
            return 0

    def top(self):
        if self.begin is not None:
            return self.begin.value

    def is_empty(self):
        return not bool(self.begin)