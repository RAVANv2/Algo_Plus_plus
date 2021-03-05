
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None



class Tree:
    def insert(self):
        x = int(input())

        if x == -1:
            return None

        root = Node(x)

        print(f"Enter left child of {root.data}")
        root.left = self.insert()

        print(f"Enter Right Child of {root.data}")
        root.right = self.insert()

        return root


class Pair:
    def __init__(self):
        self.branchSum = 0
        self.maxSum = 0


def findPair(root):
    p = Pair()

    if root is None:
        return p

    left = findPair(root.left)
    right = findPair(root.right)

    opt1 = left.branchSum + right.branchSum + root.data
    opt2 = left.branchSum + root.data
    opt3 = right.branchSum + root.data
    opt4 = root.data

    currSum = max(opt1, opt2, opt3, opt4)

    p.branchSum = max(left.branchSum, right.branchSum,0) + root.data

    p.maxSum = max(left.branchSum, right.branchSum, currSum)

    return p


def maxPathSum(root):
    p = findPair(root)

    return p.branchSum,p.maxSum



obj = Tree()

root=obj.insert()

print(maxPathSum(root))

