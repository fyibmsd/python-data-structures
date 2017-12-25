"""
    Binary Search Tree
    ==================
"""


class Leaf:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.sub_tree_size = 0

    def size(self):
        return self.sub_tree_size

    def set(self, value):
        node = Leaf(value)

        if self.root is None:
            self.root = node
            self.sub_tree_size += 1
            return

        current = self.root

        while True:
            if value > current.value:
                if current.right is None:
                    current.right = node
                    self.sub_tree_size += 1
                    break

                current = current.right
            elif value < current.value:
                if current.left is None:
                    current.left = node
                    self.sub_tree_size += 1
                    break

                current = current.left
            else:
                raise ValueError('Value {} exists in bst'.format(value))

    def contains(self, value):
        current = self.root

        while current:
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                return True

        return False
