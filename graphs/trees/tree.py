class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree:
    def __init__(self):
        self.root = None
    def minimum(self, node):
        if node.l:
            return self.minimum(node.l)
        else:
            return node

    def get_root(self):
        return self.root

    def _add(self, val, node):
        if node.v == val:
            return
        elif node.v > val:
            if not node.l:
                node.l = Node(val)
            else:
                self._add(val, node.l)
        else:
            if not node.r:
                node.r = Node(val)
            else:
                self._add(val, node.r)

    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _search(self, val, node):
        if val == node.v:
            return node
        elif node.v > val:
            if node.l is None:
                return None
            else:
                return self._search(val, node.l)
        else:
            if node.r is None:
                return None
            else:
                return self._search(val, node.r)

    def search(self, val):
        if self.root:
            return self._search(val, self.root)
        else:
            return None

    def _delete(self, node, val):
        if node is None:
            return node
        elif val < node.v:
            node.l = self._delete(node.l, val)
        elif val > node.v:
            node.r = self._delete(node.r, val)
        else:
            if node.l is None and node.r is None:
                node = None
            elif node.l is None:
                node = node.r
            elif node.r is None:
                node = node.l
            else:
                min_val = self.minimum(node.r)
                node.v = min_val.v
                node.r = self._delete(node.r, min_val.v)
        return node

    def delete(self, val):
        self._delete(self.root, val)


def breadth_tree(node):
    root = [node]
    result = []
    while root:
        queue = []
        for current in root:
            print(current.v)
            result.append(current.v)
            if current.l:
                queue += [current.l]
            if current.r:
                queue += [current.r]
        root = queue

    return result


def dept_traversal(root):
    if root is None:
        return
    dept_traversal(root.l)
    print(root.v)
    dept_traversal(root.r)


tree = Tree()
tree.add(3)
tree.add(1)
tree.add(5)
tree.add(4)
#         3
#      1     5
#          4
tree.add(70)
i = 0
print((i - 1) // 2)