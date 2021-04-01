import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


t = int(input())
while t:
    t -= 1
    n = input()
    s = map(int,input().split())
    s = sorted(s)
    min = float("inf")
    for i in range(0,int(n)-1):
        ans = s[i+1] - s[i]
        if ans < min:
            min = ans
    print(min)