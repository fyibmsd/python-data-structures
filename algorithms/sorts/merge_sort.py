# -*-coding:utf-8-*-
#
# author: fyibmsd
# desc: merge sort

from collections import deque


def merge(_left, _right):
    merged, _left, _right = deque(), deque(_left), deque(_right)
    while _left and _right:
        merged.append(_left.popleft() if _left[0] <= _right[0] else _right.popleft())
    merged.extend(_right if _right else _left)
    return list(merged)


def merge_sort(seq):
    l = len(seq)

    if l <= 1:
        return seq

    middle = l // 2
    left = merge_sort(seq[:middle])
    right = merge_sort(seq[middle:])

    return merge(left, right)
