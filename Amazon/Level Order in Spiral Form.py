def findSpiral(root):
    if not root:
        return []
    q = [root]
    height = -1
    prevHeight = float("-inf")
    final = []
    while q:
        size = len(q)
        height += 1
        ans = []
        while size:
            size -= 1
            node = q.pop(0)
            ans.append(node.data)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        if prevHeight < height:
            prevHeight = height
            if height % 2 == 0:
                final += ans[::-1]
            else:
                final += ans

    return final