# -*- coding: utf-8 -*-
import unittest
from src import (
    queue,
    stack,
    singly_linked_list,
    double_linked_list,
    undirected_graph
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


class TestUndirectedGraph(unittest.TestCase):
    def test_undirected_graph(self):
        # init
        self.ug0 = undirected_graph.UndirectedGraph()
        self.ug1 = undirected_graph.UndirectedGraph()
        self.ug2 = undirected_graph.UndirectedGraph()
        self.ug3 = undirected_graph.UndirectedGraph()

        self.ug1.add_edge(1, 2)

        self.ug2.add_edge(1, 2)
        self.ug2.add_edge(1, 2)

        self.ug3.add_edge(1, 2)
        self.ug3.add_edge(1, 2)
        self.ug3.add_edge(3, 1)

        # test adj
        self.assertTrue(2 in self.ug1.adj(1))
        self.assertEqual(len(self.ug1.adj(1)), 1)
        self.assertTrue(1 in self.ug1.adj(2))

        self.assertTrue(2 in self.ug2.adj(1))
        self.assertEqual(len(self.ug2.adj(1)), 2)
        self.assertTrue(1 in self.ug2.adj(2))

        self.assertTrue(2 in self.ug3.adj(1))
        self.assertTrue(3 in self.ug3.adj(1))
        self.assertEqual(len(self.ug3.adj(1)), 3)
        self.assertTrue(1 in self.ug3.adj(2))
        self.assertEqual(len(self.ug3.adj(2)), 2)

        # test degree
        self.assertEqual(self.ug1.degree(1), 1)
        self.assertEqual(self.ug1.degree(2), 1)

        self.assertEqual(self.ug2.degree(1), 2)
        self.assertEqual(self.ug2.degree(2), 2)

        self.assertEqual(self.ug3.degree(1), 3)
        self.assertEqual(self.ug3.degree(2), 2)
        self.assertEqual(self.ug3.degree(3), 1)

        # test vertices
        self.assertEqual(self.ug0.vertices(), [])
        self.assertEqual(len(self.ug0.vertices()), 0)

        self.assertEqual(self.ug1.vertices(), [1, 2])
        self.assertEqual(len(self.ug1.vertices()), 2)

        self.assertEqual(self.ug2.vertices(), [1, 2])
        self.assertEqual(len(self.ug2.vertices()), 2)

        self.assertEqual(self.ug3.vertices(), [1, 2, 3])
        self.assertEqual(len(self.ug3.vertices()), 3)

        # test vertex count
        self.assertEqual(self.ug0.vertex_count(), 0)
        self.assertEqual(self.ug1.vertex_count(), 2)
        self.assertEqual(self.ug2.vertex_count(), 2)
        self.assertEqual(self.ug3.vertex_count(), 3)

        # test edge count
        self.assertEqual(self.ug0.edge_count(), 0)
        self.assertEqual(self.ug1.edge_count(), 1)
        self.assertEqual(self.ug2.edge_count(), 2)
        self.assertEqual(self.ug3.edge_count(), 3)
