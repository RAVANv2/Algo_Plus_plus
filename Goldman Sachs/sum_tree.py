def sum(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.data

    return sum(root.left) + sum(root.right) + root.data

def isSumTree(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    return (root.data == sum(root.left) + sum(root.right))
