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
    h,x,y,c = amap()
    if (x + y // 2)*h <= c:
        print("YES")
    else:
        print("NO")