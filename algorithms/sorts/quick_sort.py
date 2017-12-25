# coding: utf-8
#
# author: fyibmsd
# desc: quick sort


def quick_sort(seq):
    if len(seq) <= 1:
        return seq

    pivot = seq[0]
    left, right = [], []

    for i in seq[1:]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)
