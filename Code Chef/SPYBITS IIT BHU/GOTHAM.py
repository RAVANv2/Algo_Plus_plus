import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


def aint(): return int(input())


def amap(): return map(int, input().strip().split())


def alist(): return list(map(int, input().strip().split()))


def astr(): return input().strip()


n = aint()
p = alist()
q = aint()

cap = {}
for i in range(1, n + 1):
    cap[i] = p[i - 1]
while q:
    q -= 1
    d, people = amap()
    ans = 0
    lvl = d
    if people > cap[d]:
        people = people - cap[d]
        cap[d] = 0
        for i in range(d + 1, n + 1):
            ans += people
            people = people - cap[i]
            if people <= 0:
                break
