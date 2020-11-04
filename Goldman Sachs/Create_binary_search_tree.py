class tree:
	def __init__(self,item):
		self.data = item
		self.right = self.left = None


def insert(root,key):
	if root is None:
		return tree(key)

	if root.data > key:
		root.left = insert(root.left,key)

	elif root.data < key:
		root.right = insert(root.right,key)

	return root

def inorder(root):
	if root:
		inorder(root.left)
		print(root.data, key = ' ')
		inorder(root.right)


if __name__ == "__main__":
	print("Enter root element")
	key = int(input())
	root = insert(root,key)

	while True:
		key = int(input())

		if key == -1:
			break

		root = insert(root,key)

	inorder(root)