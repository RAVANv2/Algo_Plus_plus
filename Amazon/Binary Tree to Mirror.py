def mirror(root):
    if root:
        mirror(root.left)
        mirror(root.right)
        root.left,root.right = root.right,root.left