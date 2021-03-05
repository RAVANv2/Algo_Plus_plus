def LCA(root, n1, n2):
    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root

    left = LCA(root.left, n1, n2)
    right = LCA(root.right, n1, n2)

    if left and right:
        return root

    if left:
        return left

    return right
