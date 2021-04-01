import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


r,o,c = list(map(int,input().strip().split()))

remain = 20 - o

runs = remain * 6 * 6
if runs + c > r:
    print("YES")
else:
    print("NO")
