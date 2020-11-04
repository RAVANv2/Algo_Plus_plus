class Node:
	def __init__(self,key):
		self.data = key
		self.right = self.left = None

def insert(root,key):
	if root is None:
		return Node(key)

	if root.data>key:
		root.left = insert(root.left,key)

	else:
		root.right = insert(root.right,key)

	return root

def find_min(root):
	if root:
		current = root
		while current.left is not None:
			current = current.left

		return current.data

root = None
root = insert(root,4) 
root =insert(root,2) 
root =insert(root,1) 
root =insert(root,3) 
root =insert(root,6) 
root =insert(root,5) 

print(find_min(root))

