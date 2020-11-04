class Node:
    def __init__(self,item):
        self.data = item
        self.right = self.left = None


class treeMethods:

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)
    
    def successor(self,root):
        cur = root
        while cur.left:
            cur = cur.left
        return cur

    def height(self,root):
        if root is None:
            return 0

        return 1 + max(self.height(root.right),self.height(root.left))
    
    def deleteNode(self,root,key):
        
        if root is None:
            raise Exception("root is None")

        if root.data > key:
            root.left = self.deleteNode(root.left,key)
        elif root.data < key:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.left is None:
                temp = root.right
                root.right = None
                return temp

            elif root.right is None:
                temp = root.left
                root.left = None
                return temp
            
            else:
                inorder_suc = self.successor(root.right)
                root.data = inorder_suc.data
                root.right = self.deleteNode(root.right,inorder_suc.data)
        return root

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(9)
    root.right.right = Node(20)

    obj = treeMethods()
    obj.inorder(root)
    print()
    # Delete Node
    key = 5
    d_node = obj.deleteNode(root,3)
    d_node = obj.deleteNode(d_node,9)
    d_node = obj.deleteNode(d_node,20)
    obj.inorder(d_node)
    print()
    print(obj.height(d_node))