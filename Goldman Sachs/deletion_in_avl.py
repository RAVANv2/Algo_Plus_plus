# main
def deletion(root,key):
    if root is None:
        return root

    if key<root.data:
        root.left = deletion(root.left,key)
    elif key>root.data:
        root.right = deletion(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = get_min(root.right)
        root.data = temp.data
        root.right = deletion(root.right,temp.data)

    if root is None:
        return root

    root.height  = 1+max(height(root.left),height(root.left))
    balance = get_balance(root)

    # left-Left
    if balance>1 and get_balance(root.left)>=0:
        return rightRotate(root)

    # right-right
    if balance<-1 and get_balance(root.right)<=0:
        return leftRotate(root)

    # right-left
    if balance<-1 and get_balance(root.right)>0:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    # left-right
    if balance>1 and get_balance(root.left)<0:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    return root

def get_min(root):
    temp = root
    while temp.left is not None:
        temp = temp.left
    return temp

def leftRotate(root):
    y = root.right
    t = y.left

    y.left = root
    root.right = t

    root.height = 1+max(height(root.left),height(root.right))
    y.height = 1+max(height(root.left),height(root.right))
    return y

def rightRotate(root):
    y = root.left
    y = y.right

    y.right = root
    root.left = t

    root.height = 1+max(height(root.left),height(root.right))
    y.height = 1+max(height(root.left),height(root.right))
    return y

def get_balance(root):
    if root is None:
        return 0

    return height(root.left) - height(root.right)

def height(root):
    if root is None:
        return 0

    return root.height
