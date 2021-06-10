# ds for storing data, it's FIFO which means first in first out
# BIG O
# Access:0(n)
# Insert: O(1)
# Deletion:O(1)
# Search:O(N)

class Queue:
    def __init__(self):
        self.head = []

    def add(self, item):
        node = self.head
        node.append(item)

    def print(self):
        node = self.head
        print(node)

    def remove(self):
        node = self.head
        if len(node) == 0:
            return []
        else:
            node.pop(0)

    def peek(self):
        node = self.head
        if len(node) == 0:
            return []

        print(node[0])

    def isEmpty(self):
        node = self.head
        if len(node) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    a = Queue()
    a.add(4)
    a.add(8)
    a.print()
    a.peek()
    print(a.isEmpty())
    a.isEmpty()
