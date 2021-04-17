import sys

sys.setrecursionlimit(10 ** 6)
try:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
except:
    pass


def aint(): return int(input())


def amap(): return map(int, input().strip().split())


def alist(): return list(map(int, input().strip().split()))


def astr(): return input().strip()


t = aint()

while t:
    t -= 1
    n = aint()
    rank = alist()
    curAns = float("-inf")
    for i in range(n):
        curAns = max(curAns, rank[(i - 1 + n) % n] + rank[i] + rank[(i+n) % n])
    print(curAns)
