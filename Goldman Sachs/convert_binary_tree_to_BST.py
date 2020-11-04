class Node:
	def __init__(self,item):
		self.data = item
		self.right = self.left = None

def inorder(root,arr):
	if root:
		inorder(root.left,arr)
		arr.append(root.data)
		inorder(root.right,arr)

def print_inorder(root):
	if root:
		print_inorder(root.left)
		print(root.data,end=' ')
		print_inorder(root.right)

def convert(root,arr):
	if root is None:
		return

	convert(root.left,arr)
	root.data = arr.pop(0)
	convert(root.right,arr)


def convert_to_bst(root):
	arr = []
	inorder(root,arr)
	arr = sorted(arr)
	convert(root,arr)

if __name__ == "__main__":
	root = Node(10) 
	root.left = Node(30) 
	root.right = Node(15) 
	root.left.left = Node(20) 
	root.right.right = Node(5) 

	convert_to_bst(root)
	print_inorder(root)
