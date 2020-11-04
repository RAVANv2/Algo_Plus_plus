

class Node:
	def __init__(self,item):
		self.data = item
		self.left = self.right = None

def inorder(root):
	if root:
		inorder(root.left)
		print(root.data,end=' ')
		inorder(root.right)

def delete_rightmost_node(root,node_d):
	q = []
	q.append(root)
	while len(q):
		temp = q.pop(0)
		if temp is node_d:
			temp = None
			return
		if temp.left:
			if temp.left is node_d:
				temp.left = None
				return
			else:
				q.append(temp.left)
		if temp.right:
			if temp.right is node_d:
				temp.right = None
				return
			else:
				q.append(temp.right)

def delete_node(root,key):
	if root is None:
		return root

	if root.left is None and root.right is None:
		if root.data == key:
			return None
		else:
			return root 

	q = []
	key_node = None
	q.append(root)
	while len(q):
		node = q.pop(0)
		if node.data == key:
			key_node = node
		if node.left:
			q.append(node.left)
		if node.right:
			q.append(node.right)
	if key_node:
		x = node.data
		delete_rightmost_node(root,node)
		key_node.data = x
	return root



if __name__ == "__main__":
	root = Node(10) 
	root.left = Node(11) 
	root.left.left = Node(7) 
	root.left.right = Node(12) 
	root.right = Node(9) 
	root.right.left = Node(15) 
	root.right.right = Node(8)

	inorder(root)

	key = 10

	delete_root = delete_node(root,key)

	print()

	inorder(delete_root)