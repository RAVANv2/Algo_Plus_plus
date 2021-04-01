import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

t = int(input())

while t:
    t -= 1
    n = input()
    arr = list(map(int,input().split()))
    k = int(input())
    ele = arr[k-1]
    sort_arr = sorted(arr)
    print(sort_arr.index(ele) + 1)


