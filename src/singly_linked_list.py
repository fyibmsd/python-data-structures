"""
    Singly Linked List

"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def set_data(self, value):
        self.data = value

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, value):
        """
        Add element to list
        T=O(1)
        """
        node = Node(value)
        node.set_next(self.head)
        self.head = node
        self.size += 1

    def search_node(self, value, remove=False):
        current = self.head
        previous = None

        while current:
            if current.data == value:
                break
            else:
                previous = current
                current = current.next

        if remove and current:
            if previous is None:
                self.head = current.next
            else:
                previous.set_next(current.next)
            self.size -= 1

        return current is not None

    def remove(self, value):
        return self.search_node(value, True)

    def size(self):
        return self.size
