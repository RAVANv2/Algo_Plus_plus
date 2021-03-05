
class node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def count(self, root):
        if root is None:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)

    def sum(self, root):
        if root is None:
            return 0
        return root.data + self.sum(root.left) + self.sum(root.right)

root = node(8)
root.left = node(16)
root.left.left = node(6)
root.left.right = node(4)
root.right = node(3)
root.right.left = node(2)

obj = Tree()
print(obj.count(root))
print()
print(obj.sum(root))
