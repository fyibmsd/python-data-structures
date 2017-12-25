# -*-coding:utf-8-*-
#
# author: fyibmsd
# desc: selection sort


def selection_sort(seq):
    l = len(seq)

    for i in range(0, l):
        min = i
        for j in range(i + 1, l):
            if seq[j] < seq[min]:
                min = j

        if i != min:
            seq[i], seq[min] = seq[min], seq[i]

    return seq
