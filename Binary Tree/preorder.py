class node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Tree:
    def recPreorder(self,root):
        if root:
            print(root.data, end=' ')
            self.recPreorder(root.left)
            self.recPreorder(root.right)

    def preorder(self,root):
        stack = []
        stack.append(root)
        while stack:
            newNode = stack.pop()
            print(newNode.data, end=' ')
            if newNode.right:
                stack.append(newNode.right)
            if newNode.left:
                stack.append(newNode.left)


obj = Tree()

root = node(4)
root.left = node(5)
root.left.left = node(7)
root.left.left.right = node(8)
root.right = node(6)

obj.recPreorder(root)
print()
obj.preorder(root)