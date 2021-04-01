import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


n = int(input())

arr = list(map(int,input().split()))

countEven = 0
countOdd = 0
ele_Even = -1
ele_Odd = -1
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        countEven += 1
        ele_Even = arr[i]
    else:
        countOdd += 1
        ele_Odd = arr[i]

if countEven == 1:
    print(arr.index(ele_Even)+1)
else:
    print(arr.index(ele_Odd)+1)



