import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


n = int(input())

arr = list(map(int,input().split()))

idx = []
for i in range(1,len(arr)+1):
    idx.append([arr[i-1],i])

sort_idx = sorted(idx)
ans = []
print(sort_idx)
print(idx)
for i in range(len(arr)):
    if abs(sort_idx[i][1] - idx[i][1]) >= 1:
        ans.append(idx[i][1])

if len(ans) == 2:
    print("yes")
    print(*ans)
else:
    print("no")



