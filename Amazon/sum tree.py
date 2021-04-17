def sum_tree(root):
    if not root:
        return 0

    if root.left is None and root.right is None:
        return root.data

    return sum_tree(root.left) + sum_tree(root.right) + root.data


def isSumTree(root):
    if not root:
        return 1

    if root.left is None and root.right is None:
        return 1

    return root.data == sum_tree(root.left) + sum_tree(root.right)