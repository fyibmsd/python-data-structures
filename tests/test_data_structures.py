# -*- coding: utf-8 -*-
import unittest
from src import (
    queue,
    stack,
    singly_linked_list,
    double_linked_list,
    undirected_graph,
    binary_search_tree,
    priority_queue,
    binary_tree
)


class TestQueue(unittest.TestCase):
    def exec_queue_test(self, queue):
        self.queue = queue()

        for item in [1, 2, 8, 5, 6]:
            self.queue.enqueue(item)

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.size(), 4)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 8)
        self.assertEqual(self.queue.dequeue(), 5)
        self.assertFalse(self.queue.is_empty())

    def test_queue_using_array(self):
        self.exec_queue_test(queue.QueueUsingArray)

    def test_queue_using_linked_list(self):
        self.exec_queue_test(queue.QueueUsingLinkedList)


class TestStack(unittest.TestCase):
    def exec_stack_test(self, stack):
        self.stack = stack()

        for item in [1, 2, 8, 5, 6]:
            self.stack.add(item)

        self.assertEqual(self.stack.remove(), 6)
        self.assertEqual(self.stack.size(), 4)
        self.assertEqual(self.stack.remove(), 5)
        self.assertEqual(self.stack.remove(), 8)
        self.assertEqual(self.stack.remove(), 2)
        self.assertFalse(self.stack.is_empty())

    def test_stack_using_array(self):
        self.exec_stack_test(stack.StackUsingArray)

    def test_stack_using_linked_list(self):
        self.exec_stack_test(stack.StackUsingLinkedList)


class TestPrioirtyQueue(unittest.TestCase):
    def test_priority_queue(self):
        queue = priority_queue.PriorityQueue()
        self.assertTrue(queue.is_empty())
        queue.insert('A', 10)
        queue.insert('B', 20)
        queue.insert('C', 5)

        self.assertEqual(queue.size(), 3)

        self.assertEqual(queue.dequeue(), ('B', 20))
        self.assertEqual(queue.dequeue(), ('A', 10))
        self.assertEqual(queue.dequeue(), ('C', 5))


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


class TestBinaryTree(unittest.TestCase):
    """
        url: https://en.wikipedia.org/wiki/Tree_traversal
                    F
                 /     \
              B           G
            /   \           \
           A     D           I
               /  \         /
              C    E       H

        Pre-order: F, B, A, D, C, E, G, I, H.
    """

    def create_tree(self):
        tree = binary_tree.BinaryTree()
        tree.root = binary_tree.Leaf('F')

        tree.root.left = binary_tree.Leaf('B')
        tree.root.left.left = binary_tree.Leaf('A')
        tree.root.left.right = binary_tree.Leaf('D')
        tree.root.left.right.left = binary_tree.Leaf('C')
        tree.root.left.right.right = binary_tree.Leaf('E')

        tree.root.right = binary_tree.Leaf('G')
        tree.root.right.right = binary_tree.Leaf('I')
        tree.root.right.right.left = binary_tree.Leaf('H')

        return tree

    def test_invert(self):
        tree = self.create_tree()
        self.assertEqual(str(tree), "FBADCEGIH")

        tree.invert(tree.root)

        # tree.pretty_print()
        self.assertEqual(str(tree), "FGIHBDECA")

    def test_traversal(self):
        tree = self.create_tree()

        self.assertEqual(tree.pre_order(tree.root), "FBADCEGIH")
        self.assertEqual(tree.in_order(tree.root), "ABCDEFGHI")
        self.assertEqual(tree.post_order(tree.root), "ACEDBHIGF")


class TestBinarySearchTree(unittest.TestCase):

    def test_size(self):
        self.bst = binary_search_tree.BinarySearchTree()
        self.assertEqual(self.bst.size(), 0)

    """
                    4
                 /     \
              2           6
            /   \       /   \
           1     3     5     7
          -^--^--^--^--^--^--^-
           1  2  3  4  5  6  7
    """

    def test_bst(self):
        self.bst = binary_search_tree.BinarySearchTree()

        self.assertEqual(self.bst.contains(2), False)

        for i in [4, 2, 6, 1, 3, 5, 7]:
            self.bst.set(i)

        self.assertEqual(self.bst.size(), 7)
        self.assertTrue(self.bst.contains(5))
        self.assertFalse(self.bst.contains(8))
