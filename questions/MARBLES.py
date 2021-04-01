import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


t = int(input())

while t:
    t -= 1
    n,k = list(map(int,input().split()))
    n -= 1
    k -= 1
    c = r = 1
    if k < n - k:
        r = k
    else:
        r = n - k
    for i in range(r):
        c = c * (n - i) // (i + 1)
    print(c)