
class node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def diameter(self, root):

        if root is None:
            return 0

        h1 = self.height(root.left)
        h2 = self.height(root.right)

        opt1 = h1 + h2
        opt2 = self.diameter(root.left)
        opt3 = self.diameter(root.right)

        return max(opt2, opt1, opt2)



root = node(8)
root.left = node(16)
root.left.left = node(6)
root.left.right = node(4)
root.right = node(3)
root.right.left = node(2)

obj = Tree()
print(obj.diameter(root))
