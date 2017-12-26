# -*- coding: utf-8 -*-
import unittest

from src.undirected_graph import UndirectedGraph
from algorithms.sorts import (
    bubble_sort, quick_sort, insertion_sort, selection_sort, merge_sort
)
from algorithms.deep_first_search import DeepFirstSearch


class TestSort(unittest.TestCase):
    def exec_sort(self, sort_func):
        unsorted = [6, 5, 3, 1, 8, 7, 2, 4]
        self.assertEqual(sort_func(unsorted), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_sorts(self):
        self.exec_sort(bubble_sort.bubble_sort)
        self.exec_sort(quick_sort.quick_sort)
        self.exec_sort(insertion_sort.insertion_sort)
        self.exec_sort(selection_sort.selection_sort)
        self.exec_sort(merge_sort.merge_sort)


class TestDFS(unittest.TestCase):
    def test_dfs(self):
        """
               0
           /   |   \
          5    1 -- 2
           \     /   \
              3   --  4
        """
        # init
        self.ug = UndirectedGraph()
        for src, dest in [[0, 1], [0, 2], [0, 5], [1, 2],
                          [2, 3], [2, 4], [3, 4], [3, 5]]:
            self.ug.add_edge(src, dest)

        DeepFirstSearch(self.ug, 0)
