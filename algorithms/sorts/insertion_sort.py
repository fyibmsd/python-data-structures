# -*-coding:utf-8-*-
#
# author: fyibmsd
# desc: insertion sort


def insertion_sort(seq):
    l = len(seq)

    for i in range(1, l):
        item = seq[i]
        hole = i
        while hole > 0 and seq[hole - 1] > item:
            seq[hole] = seq[hole - 1]
            hole -= 1
        seq[hole] = item

    return seq
