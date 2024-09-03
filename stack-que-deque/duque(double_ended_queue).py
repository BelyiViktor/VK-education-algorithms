class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None


class Deque:
    def push_back(self, value):
        new_node = Node(value)
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        new_node.next = self.tail

