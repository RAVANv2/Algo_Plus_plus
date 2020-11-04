def hasPathSum(root, sm):
    if (root is None or sm==0):
        return 0
        
    if(root.left is None and root.right is None):
        return (sm-root.data==0)

    return (hasPathSum(root.left,sm-root.data) or hasPathSum(root.right,sm-root.data))
