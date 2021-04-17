def print_sib(node,ans):
    if not node:
        return
    if node.left is None and node.right:
        ans.append(node.right.data)
    if node.right is None and node.left:
        ans.append(node.left.data)
    print_sib(node.left,ans)
    print_sib(node.right,ans)

def noSibling(root):

    ans = []
    print_sib(root,ans)
    if ans:
        return ans
    else:
        return [-1]