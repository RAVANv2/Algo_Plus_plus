# Method 1 (DFS)
def printLeftView(root, lvl, maxlvl, ele):
    if root is None:
        return

    if lvl > maxlvl[0]:
        ele.append(root.data)
        maxlvl[0] = lvl

    printLeftView(root.left, lvl + 1, maxlvl, ele)
    printLeftView(root.right, lvl + 1, maxlvl, ele)

def LeftView(root):
    maxlvl = [-1]
    ele = []
    printLeftView(root, 0, maxlvl, ele)
    return ele

# Method 2(BFS)
def LeftView_(root):
    ele = []
    q = []
    q.append(root)
    height = 0
    prev = 0
    while q:
        size = len(q)
        height += 1
        while size:
            size -= 1
            node = q.pop(0)
            if height > prev:
                ele.append(node.data)
                prev = height
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return ele

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.left.right = Node(8)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

print(LeftView(root))