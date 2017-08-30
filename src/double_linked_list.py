"""
    Double Linked List

"""


class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None

    def set_data(self, value):
        self.data = value

    def get_data(self):
        return self.data

    def set_prev(self, node):
        self.prev = node

    def set_next(self, node):
        self.next = node


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def lpush(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            if self.tail is None:
                self.tail = self.head
        else:
            node.set_next(self.head)
            self.head.set_prev(node)
            self.head = node

        self.size += 1

    def rpush(self, value):
        node = Node(value)

        if self.tail is None:
            self.tail = node
            if self.head is None:
                self.head = self.tail
        else:
            node.set_prev(self.tail)
            self.tail.set_next(node)
            self.tail = node

        self.size += 1

    def lpop(self):
        if self.head is None:
            return False

        return self.remove(self.head)

    def rpop(self):
        if self.tail is None:
            return False

        return self.remove(self.tail)

    def insert_at(self, current, value):
        node = Node(value)
        node.set_next(current.next)
        current.next.set_prev(node)
        node.set_prev(current)
        current.set_next(node)
        self.size += 1

    def remove(self, node):
        current = node

        if current.prev is not None:
            current.prev.next = node.next
        else:
            self.head = node.next

        if current.next is not None:
            current.next.prev = node.prev
        else:
            self.tail = node.prev

        self.size -= 1

        return node.data

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0
