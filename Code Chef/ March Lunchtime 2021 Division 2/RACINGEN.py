import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

t = int(input())

while t:
    t -= 1
    x,r,m = list(map(int,input().strip().split()))
    time = abs(r-m)
    if (time*x - x*r + x) < 0:
        print("No")
    else:
        print("Yes")