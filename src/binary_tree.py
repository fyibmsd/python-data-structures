# -*-coding:utf-8-*-
#
# author: fyibmsd
# desc: binary tree

from StringIO import StringIO
from .queue import QueueUsingArray as Queue
import math


class Leaf:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value


class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return self.pre_order(self.root)

    def invert(self, node):
        if node is not None:
            node.left, node.right = node.right, node.left
            if node.left is not None:
                node.left = self.invert(node.left)
            if node.right is not None:
                node.right = self.invert(node.right)

        return node

    def pre_order(self, node):
        return node.value + self.pre_order(node.left) + self.pre_order(node.right) \
            if node is not None else ""

    def in_order(self, node):
        return self.in_order(node.left) + node.value + self.in_order(node.right) \
            if node is not None else ""

    def post_order(self, node):
        return self.post_order(node.left) + self.post_order(node.right) + node.value \
            if node is not None else ""

    def pretty_print(self):
        output = StringIO()
        pretty_output = StringIO()
        depth = 0

        current_level = Queue()
        next_level = Queue()
        current_level.enqueue(self.root)

        if self.root is not None:
            while not current_level.is_empty():
                current_node = current_level.dequeue()
                output.write('%s ' % current_node.value if current_node else '# ')

                next_level.enqueue(current_node.left if current_node else current_node)
                next_level.enqueue(current_node.right if current_node else current_node)

                if current_level.is_empty():
                    if sum([i is not None for i in next_level._queue]):
                        current_level, next_level = next_level, current_level
                        depth += 1
                        output.write('\n')

        output.seek(0)
        pad_length = 3
        spaces = int(math.pow(2, depth))

        def add_padding(str, pad_length_value):
            str = str.strip()
            return str.center(pad_length_value, ' ')

        while spaces > 0:
            skip_start = spaces * pad_length
            skip_mid = (2 * spaces - 1) * pad_length

            key_start_spacing = ' ' * skip_start
            key_mid_spacing = ' ' * skip_mid

            keys = output.readline().split(' ')  # read one level to parse
            padded_keys = (add_padding(key, pad_length) for key in keys)
            padded_str = key_mid_spacing.join(padded_keys)
            complete_str = ''.join([key_start_spacing, padded_str])

            pretty_output.write(complete_str)

            # add space and slashes to middle layer
            slashes_depth = spaces
            spaces = spaces // 2
            if spaces > 0:
                pretty_output.write('\n')  # print '\n' each level

                cnt = 0
                while cnt < slashes_depth:
                    inter_symbol_spacing = ' ' * (pad_length + 2 * cnt)
                    symbol = ''.join(['/', inter_symbol_spacing, '\\'])
                    symbol_start_spacing = ' ' * (skip_start - cnt - 1)
                    symbol_mid_spacing = ' ' * (skip_mid - 2 * (cnt + 1))
                    pretty_output.write(''.join([symbol_start_spacing, symbol]))
                    for i in keys[1:-1]:
                        pretty_output.write(''.join([symbol_mid_spacing, symbol]))
                    pretty_output.write('\n')
                    cnt = cnt + 1

        print(pretty_output.getvalue())
