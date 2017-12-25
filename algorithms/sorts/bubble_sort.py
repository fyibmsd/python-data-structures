# coding: utf-8
# author: fyibmsd


def bubble_sort(seq):
    l = len(seq)

    for i in range(l):
        for j in range(1, l - i):
            if seq[j] < seq[j - 1]:
                seq[j - 1], seq[j] = seq[j], seq[j - 1]

    return seq
