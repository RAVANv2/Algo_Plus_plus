

class node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None


class Tree:
    def levelOrder(self,root):
        queue = []
        queue.append(root)

        while queue:
            new = queue.pop(0)
            print(new.data, end=' ')
            if new.left:
                queue.append(new.left)
            if new.right:
                queue.append(new.right)

    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height((root.right)))

    def levelOrderRec(self, root, k):
        if root is None:
            return

        if k == 1:
            print(root.data, end=' ')

        self.levelOrderRec(root.left, k-1)
        self.levelOrderRec(root.right,k-1)


root = node(1)
root.left = node(2)
root.left.left = node(4)
root.left.right = node(5)

root.right = node(3)
root.right.left = node(6)
root.right.right = node(7)

obj = Tree()
obj.levelOrder(root)
print()

# Getting height of tree for levelOrder with recursion
height = obj.height(root)
for h in range(1,height+1):
    obj.levelOrderRec(root,h)