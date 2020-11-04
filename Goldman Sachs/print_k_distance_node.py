class tree:
	def __init__(self,item):
		self.data = item
		self.left = self.right = None

def print_k_dist_node(root,k):
	if not root:
		return

	if k==0:
		print(root.data)
		return
	else:
		print_k_dist_node(root.left,k-1)
		print_k_dist_node(root.right,k-1)



if __name__ == "__main__":
	root = tree(6)
	root.left = tree(7)
	root.right = tree(5)
	root.left.left = tree(4)
	root.left.right = tree(2)
	root.right.right = tree(1)

	k = 1
	print(print_k_dist_node(root,k))