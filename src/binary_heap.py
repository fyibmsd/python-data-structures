# -*-coding:utf-8-*-
#
# author: fyibmsd
# desc: binary heap


class MaxBinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)

        i = len(self.heap) - 1

        def parent(index):
            return (index - 1) // 2

        while i > 0 and self.heap[i] > self.heap[parent(i)]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[parent(i)]
            self.heap[parent(i)] = tmp
            i = parent(i)

    def remove_max(self):
        i = 0
        top = self.heap[i]

        if len(self.heap) is 1:
            return self.heap.pop()

        self.heap[i] = self.heap.pop(len(self.heap) - 1)

        def sub(index):
            return index * 2 + 1

        while sub(i) < len(self.heap):
            if self.heap[i] < self.heap[sub(i)]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[sub(i)]
                self.heap[sub(i)] = tmp
                i = sub(i)
            else:
                return top

        return top
