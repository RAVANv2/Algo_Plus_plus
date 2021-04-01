import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


def pint(): return int(input())
def pmap(): return map(int, input().strip().split())
def plist(): return list(map(int, input().strip().split()))
def pstr(): return input().strip()

def neg(d):
    if d[0] < 0: return True
    else: return False
def posidx(d):
    for i in range(len(d)):
        if d[i] > 0:
            return i
t = int(input())
while t:
    t -= 1
    n = pint()
    l = plist()
    premin = [0] * n
    premax = [0] * n
    sufmin = [0] * n
    sufmax = [0] * n
    premin[0] = premax[0] = l[0]
    sufmin[-1] = sufmax[-1] = l[-1]
    for i in range(1, n):
        premin[i] = min(premin[i - 1], 0) + l[i]
        premax[i] = max(premax[i - 1], 0) + l[i]
    for i in range(n - 2, -1, -1):
        sufmin[i] = min(sufmin[i + 1], 0) + l[i]
        sufmax[i] = max(sufmax[i + 1], 0) + l[i]
    ans = 0
    print(sufmax,sufmin)
    print(premax, premin)
    print("^"*10)

