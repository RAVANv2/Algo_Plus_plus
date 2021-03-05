def check(l, r):
    if l is None and r is None:
        return True

    if l and r and l.data == r.data:
        return check(l.left, r.right) and check(l.right, r.left)

    return False


# Main Function
def isSymmetric(root):
    if root is None:
        return True

    return check(root.left, root.right)
