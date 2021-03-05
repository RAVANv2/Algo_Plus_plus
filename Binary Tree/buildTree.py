
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None



class Tree:
    def insert(self):
        x = int(input())

        if x == -1:
            return None

        root = Node(x)

        print(f"Enter left child of {root.data}")
        root.left = self.insert()

        print(f"Enter Right Child of {root.data}")
        root.right = self.insert()

        return root

    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)



obj = Tree()

root=obj.insert()
obj.inorder(root)
