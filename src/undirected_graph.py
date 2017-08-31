# -*- coding: utf-8 -*-
"""
    Undirected Graph

    http://btechsmartclass.com/DS/U3_T8.html
"""


class UndirectedGraph:
    def __init__(self):
        self.adjacent = {}
        self.v_count = 0
        self.e_count = 0

    def vertex_count(self):
        """
        返回顶点的数量
        T=O(1)
        """
        return self.v_count

    def edge_count(self):
        """
        返回边的数量
        T=O(1)
        """
        return self.e_count

    def add_edge(self, src, dest):
        """
        添加无向边(undirected edge) 'src' - 'dest'
        T=O(1)
        """
        if src in self.adjacent:
            self.adjacent[src].append(dest)
        else:
            self.adjacent[src] = [dest]
            self.v_count += 1

        if dest in self.adjacent:
            self.adjacent[dest].append(src)
        else:
            self.adjacent[dest] = [src]
            self.v_count += 1

        self.e_count += 1

    def adj(self, src):
        """
        返回与src顶点相邻的顶点
        T=O(1)
        """
        return self.adjacent[src]

    def degree(self, src):
        """
        返回顶点的度
        T=O(1)
        """
        if src in self.adjacent:
            return len(self.adjacent[src])
        else:
            raise LookupError("This vertex is not in the graph")

    def vertices(self):
        """
        返回图中所有顶点的集合
        T=O(1)
        """
        return self.adjacent.keys()
