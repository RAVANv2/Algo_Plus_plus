def find_hd(root,hd,lvl):
    if root:
        find_hd(root.left,hd,lvl-1)
        hd[root.data] = lvl
        find_hd(root.right,hd,lvl+1)
    return hd

class Solution:
    def verticalOrder(self, root):
        hd = {}
        hd =find_hd(root,hd,0)
        distance = [k for k,v in sorted(hd.items(), key = lambda x:x[1])]
        return distance
    