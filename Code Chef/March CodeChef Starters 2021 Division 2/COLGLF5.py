import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


t = int(input())

while t:
    t -= 1
    n,m = list(map(int,input().strip().split()))
    foot = list(map(int,input().strip().split()))
    cri = list(map(int,input().strip().split()))

    ans = {}
    for i in foot:
        ans[i] = "foot"
    for i in cri:
        ans[i] = "cri"
    com = sorted(foot + cri)
    count = 0
    flag = "foot"
    for i in com:
        if ans[i] == flag:
            continue
        else:
            count += 1
            flag = ans[i]
    print(count)