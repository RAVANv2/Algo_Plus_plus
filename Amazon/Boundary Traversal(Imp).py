def left(root, res):
    if not root:
        return res

    if root.left:
        res.append(root.data)
        res = left(root.left, res)
    elif root.right:
        res.append(root.data)
        res = left(root.right, res)
    return res


def print_leaves(root, res):
    if not root:
        return res

    if not root.left and not root.right:
        res.append(root.data)

    res = print_leaves(root.left, res)
    res = print_leaves(root.right, res)
    return res


def right(root, res):
    if not root:
        return res

    if root.right:
        res = right(root.right, res)
        res.append(root.data)
    elif root.left:
        res = right(root.left, res)
        res.append(root.data)
    return res


# Main
def printBoundaryView(root):
    res = [root.data]

    res = left(root.left, res)
    res = print_leaves(root.left, res)
    res = print_leaves(root.right, res)
    res = right(root.right, res)

    return res