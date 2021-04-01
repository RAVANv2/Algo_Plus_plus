import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


t = int(input())

while t:
    t -= 1
    n = int(input())
    arr = list(map(int,input().strip().split()))

    p = 0
    final = 0
    for i in range(n-1,-1,-1):
        if arr[i] > p:
            final += arr[i] - p
            p = arr[i] - 1
        else:
            p = min(arr[i],p) - 1
    print(final)