def look(root, l, r):
    if root is None:
        return True

    if (l != None and l.data >= root.data):
        return False

    if (r != None and r.data <= root.data):
        return False

    return (look(root.left, l, root) and look(root.right, root, r))


def isBST(root):
    ans = look(root, None, None)
    return ans
