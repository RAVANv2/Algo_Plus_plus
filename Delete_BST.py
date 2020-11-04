class Node:
	def __init__(self,key):
		self.data = key
		self.left = self.right = None


# Driver program to test above functions 
""" Let us create following BST 
              50 
           /     \
          30      70 
         /  /    /    \
       20   40  60   80 """

def insert(root,key):
	if root is None:
		return Node(key)

	if root.data<key:
		root.right =  insert(root.right,key)
	else:
		root.left =  insert(root.left,key)

	return root
  
root = None
root = insert(root, 50) 
root = insert(root, 30) 
root = insert(root, 20) 
root = insert(root, 40) 
root = insert(root, 70) 
root = insert(root, 60) 
root = insert(root, 80) 


def inorder(root):
	if root:
		inorder(root.left)
		print(root.data,end=' ')
		inorder(root.right)

def minNode(root):
	current = root

	while current.left is not None:
		current = current.left

	return current

def deleteNode(root,key):
	if root is None:
		return root

	if(root.data>key):
		root.left = deleteNode(root.left,key)

	elif(root.data<key):
		root.right =  deleteNode(root.right,key)

	else:
		'''1-> Case (One Children)''' 
		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None: 
			temp = root.left
			root = None
			return temp

		'''3-> Case (Two Children)'''
		temp = minNode(root.right)

		root.data = temp.data

		root.right = deleteNode(root.right,temp.data)

	return root

root = deleteNode(root,50)
inorder(root)