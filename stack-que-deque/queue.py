class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1

    def pop(self):
        if self.head.next == self.tail:
            return
        pop_result = self.tail.prev
        self.tail.prev = pop_result.prev
        pop_result.prev.next = pop_result.next
        pop_result.next = None
        pop_result.prev = None
        self.size -= 1
        return pop_result.data

que = Queue()
que.push(4)
print(que.pop())