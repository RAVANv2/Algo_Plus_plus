class dll:
	def __init__(self,item):
		self.data = item
		self.left = self.right = None

def insert(root,key):
	temp = root
	while temp.right:
		temp = temp.right
	new_node = dll(key)
	temp.right = new_node
	new_node.left = temp
	return root

def insert_node(root,idx,key):
	temp = root

	while idx!=1:
		temp = temp.right
		idx -= 1

	new_node = dll(key)
	temp_next = temp.right
	temp.right = new_node
	new_node.left = temp
	new_node.right = temp_next
	temp_next.left = new_node
	return root

def print_dll(root):
	while root:
		print(root.data,end=' ')
		root = root.right

if __name__ == "__main__":

	x = int(input())
	root = dll(x)
	while True:
		key = int(input())
		if key == -1:
			break
		root = insert(root,key)
	print_dll(root)

	print("Enter the index and the key for insertion")
	idx = int(input())
	key = int(input())
	root = insert_node(root,idx,key)
	print_dll(root)	