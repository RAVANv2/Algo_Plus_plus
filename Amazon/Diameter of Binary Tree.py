def height(root):
    if not root: return 0
    return 1 + max(height(root.left), height(root.right))


def diameter(root):
    if not root:
        return 0

    left = height(root.left)
    right = height(root.right)

    opt1 = diameter(root.left)
    opt2 = diameter(root.right)

    return max(1 + left + right, opt1, opt2)
