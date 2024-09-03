class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if not self.top:
            self.top = new_node
            return

        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        top = self.top
        if self.top.next:
            self.top = self.top.next
        else:
            self.top = None
        return top.data

stack = Stack()
stack.push('1')
stack.push('3')
print(stack.pop())
print(stack.pop())
