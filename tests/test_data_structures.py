# -*- coding: utf-8 -*-
import unittest
from src import (
    queue,
    stack,
    singly_linked_list,
    double_linked_list
)


class TestQueue(unittest.TestCase):
    def test_queue(self):
        self.queue = queue.Queue()

        for item in [1, 2, 8, 5, 6]:
            self.queue.enqueue(item)

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.size(), 4)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 8)
        self.assertEqual(self.queue.dequeue(), 5)
        self.assertFalse(self.queue.is_empty())


class TestStack(unittest.TestCase):
    def test_stack(self):
        self.stack = stack.Stack()

        for item in [1, 2, 8, 5, 6]:
            self.stack.add(item)

        self.assertEqual(self.stack.remove(), 6)
        self.assertEqual(self.stack.size(), 4)
        self.assertEqual(self.stack.remove(), 5)
        self.assertEqual(self.stack.remove(), 8)
        self.assertEqual(self.stack.remove(), 2)
        self.assertFalse(self.stack.is_empty())


class TestSinglyLinkedList(unittest.TestCase):
    def test_sl_list(self):
        self.sl = singly_linked_list.SinglyLinkedList()

        for item in [10, 5, 30]:
            self.sl.add(item)

        self.assertTrue(self.sl.remove(30))
        self.assertEqual(self.sl.size, 2)
        self.assertTrue(self.sl.search_node(5))
        self.assertTrue(self.sl.remove(5))
        self.assertFalse(self.sl.search_node(5))


class TestDoubleLinkedList(unittest.TestCase):
    def test_dl_list(self):
        """
            31 <-> 41 <-> 59
        """
        self.dl = double_linked_list.DoubleLinkedList()
        self.assertEqual(self.dl.size, 0)

        self.dl.lpush(59)
        self.dl.lpush(31)

        self.assertEqual(self.dl.head.get_data(), 31)
        self.assertEqual(self.dl.tail.get_data(), 59)

        self.dl.insert_at(self.dl.head, 41)

        self.assertEqual(self.dl.size, 3)
        self.assertEqual(self.dl.rpop(), 59)
        self.assertEqual(self.dl.tail.get_data(), 41)
