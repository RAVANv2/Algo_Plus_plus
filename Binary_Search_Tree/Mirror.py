

class node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None


def insert(root,array,i,n):

    if i < n:
        new = node(array[i])
        root = new
        root.left = insert(root.left,array,2*i + 1,n)
        root.right = insert(root.right,array,2*i+2,n)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def mirror(root):
    if root is None:
        return
    else:
        mirror(root.left)
        mirror(root.right)
        root.left,root.right = root.right,root.left

array = [1, 4, 6, 2, 7, 5, 8]

root = None
root = insert(root,array,0,len(array))
mirror(root)
inorder(root)