import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


t = int(input())

while t:
    t -= 1
    n,m = list(map(int,input().strip().split()))
    arr = list(map(int,input().strip().split()))

    if len(set(arr)) == m:
        print("No")
    else:
        print("Yes")

