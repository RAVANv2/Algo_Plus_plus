head = None
pre = None


def bToDLL(root):
    global head
    global pre

    if root is None:
        return

    bToDLL(root.left)

    if(pre is None):
        head = root
        pre = root
    else:
        root.left = pre
        pre.right = root
        pre = root

    bToDLL(root.right)

    return head
