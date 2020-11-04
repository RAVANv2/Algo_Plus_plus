class tree:
	def __init__(self,item):
		self.data = item
		self.left = self.right = None

def inorder(root):
	if root:
		inorder(root.left)
		inorder_list.append(root.data)
		inorder(root.right)

def preorder(root):
	if root:
		preorder_list.append(root.data)
		preorder(root.left)
		preorder(root.right)


def create_tree(inorder_list,preorder_list,start,end):
	if start > end:
		return None

	tree_node = tree(preorder_list.pop(0))

	if start == end:
		return tree_node

	idx = search(inorder_list,start,end,tree_node.data)
	tree_node.left = create_tree(inorder_list,preorder_list,start,idx-1)
	tree_node.right = create_tree(inorder_list,preorder_list,idx+1,end)
	return tree_node

def search(inorder_list,start,end,data):
	for i in range(start,end+1):
		if inorder_list[i] == data:
			return i

def print_inorder(root):
	if root:
		print_inorder(root.left)
		print(root.data,end=' ')
		print_inorder(root.right)



if __name__ == "__main__":
	root = tree(6)
	root.left = tree(7)
	root.right = tree(5)
	root.left.left = tree(4)
	root.left.right = tree(2)
	root.right.right = tree(1)

	inorder_list = []
	preorder_list = []
	inorder(root)
	preorder(root)

	treeNode = create_tree(inorder_list,preorder_list,0,len(preorder_list)-1)
	print_inorder(treeNode)
	