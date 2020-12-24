class Node:
    def __init__(self,key):
        self.right = self.left = None
        self.data = key


def input_tree():
    x = int(input())

    if x==-1:
        return None

    temp = Node(x)

    print(f"Left Child of :{x}")
    temp.left = input_tree()

    print(f"Right Child of :{x}")
    temp.right = input_tree()

    return temp

def insert_node(root,key):
    if root is None:
        root = Node(key)
    
    else:
        if root.data>key:
            if root.left is None:
                root.left = Node(key)
            else:
                insert_node(root.left,key)
         else:
             if root.right is None:
                 root.right = Node(key)
            else:
                insert_node(root.right,key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right) 

if __name__ == "__main__":
    root = input_tree()
    insert_node(root,40)
    inorder(root)


    