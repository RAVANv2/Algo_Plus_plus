import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


def aint(): return int(input())


def amap(): return map(int, input().strip().split())


def alist(): return list(map(int, input().strip().split()))


def astr(): return input().strip()

t = aint()

while t:
    t -= 1
    n = aint()
    b = alist()
    g = alist()

    b1 = sorted(b)
    g1 = sorted(g,reverse=True)

    b2 = sorted(b,reverse=True)
    g2 = sorted(g)

    val = float("-inf")
    for i in range(n):
        like = max(b1[i]+g1[i], b2[i]+g2[i])
        if like > val:
            val = like
    print(val)