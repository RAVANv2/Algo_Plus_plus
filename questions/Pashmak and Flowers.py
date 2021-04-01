import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n = int(input())
arr = list(map(int,input().split()))

arr = sorted(arr)

min = min(arr)
max = max(arr)

if min != max:
    print(max-min,arr.count(min)*arr.count(max))
else:
    print(0,n*(n-1)//2)


