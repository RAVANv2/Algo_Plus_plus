class Node:
    def __init__(self,data):
        self.left = self.right = None
        self.height = 1
        self.data = data


def insert(root,key):
    if root is None:
        return Node(key)

    if root.data>key:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)

    root.height = 1+max(height(root.left),height(root.right))
    balance = get_balance(root)

    '''Check all the 4 cases
    1-> Left-Left'''

    if (balance>1) and (key<root.left.data):
        return rightRotate(root)

    '''2-> Right-Right'''

    if (balance<-1) and (key>root.right.data):
        return leftRotate(root)

    '''3-> Left-Right'''

    if (balance>1) and (key>root.left.data):
        root.left = leftRotate(root.left)
        return rightRotate(root)

    '''4-> Right-Left'''

    if (balance<-1) and (key<root.right.data):
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def leftRotate(root):
    y = root.right
    t = y.left
    # Interchange
    y.left = root
    root.right = t

    root.height = 1 + max(height(root.left),height(root.right))
    y.height = 1 + max(height(y.left),height(y.right))
    return y

def rightRotate(root):
    y = root.left
    t = y.right
    #Interchange
    y.right = root
    root.left = t

    root.height = 1 + max(height(root.left),height(root.right))
    y.height = 1 + max(height(y.left),height(y.right))
    return y

def get_balance(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)


def height(root):
    if root is None:
        return 0
    return root.height


def preorder(root):
    if root is not None:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)

root = Node(10)

root = insert(root, 20)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 25)

preorder(root)
