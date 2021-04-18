class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Print left view of tree
def printLeft(root, lvl, maxlvl):
    if root is None:
        return
    if maxlvl[0] < lvl:
        maxlvl[0] = lvl
        res.append(root.data)
    printLeft(root.left, lvl+1, maxlvl)
    printLeft(root.right, lvl+1, maxlvl)


def printLeftOut(root):
    if not root:
        return
    if root.left:
        print(root.data, end=" ")
        printLeftOut(root.left)
    elif root.right:
        print(root.data, end=" ")
        printLeftOut(root.right)

def leafTraversal(root):
    if not root:
        return
    leafTraversal(root.left)
    if root.left is None and root.right is None:
        print(root.data, end=" ")
    leafTraversal(root.right)

def printRightOut(root):
    if not root:
        return
    if root.right:
        printRightOut(root.right)
        print(root.data, end=" ")
    elif root.left:
        printRightOut(root.left)
        print(root.data, end=" ")


def outLine(root):
    if root:
        print(root.data, end=" ")
        printLeftOut(root.left)
        leafTraversal(root.left)
        leafTraversal(root.right)
        printRightOut(root.right)



res = []
tree = Node(1)
tree.left = Node(2)
tree.left.right = Node(6)
tree.left.left = Node(5)
tree.left.right.left = Node(7)
tree.right = Node(3)
tree.right.right = Node(6)

# printLeft(tree,0,[-1])
# print(res)

outLine(tree)