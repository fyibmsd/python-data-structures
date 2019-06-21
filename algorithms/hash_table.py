from typing import List


class Item:
    def __init__(self, key: int, val: any):
        self.key = key
        self.val = val


class HashTable:
    table: List[List[Item]]

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def set(self, key: int, val: any):
        hash_index = self._simple_hash(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.val = val
                return

        self.table[hash_index].append(Item(key, val))

    def get(self, key: int):
        hash_index = self._simple_hash(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.val
        return None

    def remove(self, key: int) -> bool:
        hash_index = self._simple_hash(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return True
        return False

    def _simple_hash(self, key: int):
        return key % self.size


def main():
    table = HashTable(10)
    table.set(1, 'hello')
    table.set(2, 'world')
    table.set(11, 'hash')

    print(table.get(1))
    print(table.get(11))
    print(table.get(3))
    print(table.remove(2))


if __name__ == '__main__':
    main()
