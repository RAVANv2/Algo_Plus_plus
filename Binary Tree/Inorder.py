

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Tree:
    def recInorder(self,root):
        if root:
            self.recInorder(root.left)
            print(root.data, end=' ')
            self.recInorder(root.right)

    def inorder(self,root):
        stack = []
        curr = root
        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                print(curr.data, end=' ')
                curr = curr.right
            else:
                break

root = Node(4)
root.left = Node(5)
root.left.left = Node(7)
root.left.left.right = Node(8)
root.right = Node(6)

obj = Tree()
obj.recInorder(root)
print()
obj.inorder(root)