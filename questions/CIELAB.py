import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


a,b = list(map(int,input().split()))

dif = a - b

if dif == 1 or dif % 10 == 0:
    dif+=1
else:
    dif-=1
print(dif)