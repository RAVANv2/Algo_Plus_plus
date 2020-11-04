class tree:
	def __init__(self,item):
		self.data = item
		self.left = self.right = None

def input_tree():

	x = int(input())

	if x==-1:
		return None

	root = tree(x)

	print(f"Enter the left child of {x}")
	root.left = input_tree()

	print(f"Enter right child of {x}")
	root.right = input_tree()

	return root

def inorder(root):
	if root:
		inorder(root.left)
		print(root.data,end=' ')
		inorder(root.right)

def preorder(root):
	if root:
		print(root.data,end = ' ')
		preorder(root.left)
		preorder(root.right)

print("Enter the root Node")
root = input_tree()
print(f'Inorder is: {inorder(root)}')
print(f'preorder is: {preorder(root)}')



