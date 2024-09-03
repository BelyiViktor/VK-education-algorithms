# АВЛ - деревья, balance(T) = T.right.height - T.left.height
# |balance(T)| <= 1, где Т - любое поддерево в данном дереве

class Node:
    def __init__(self, val):
        self.v = val
        self.p = None
        self.l = None
        self.r = None
        self.bf = 0


from tree import Tree


tree = Tree()

tree.add