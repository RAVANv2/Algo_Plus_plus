import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

from collections import defaultdict
dp = {}
dp = defaultdict(lambda:0,dp)

def solve(c):
    if c == 0:
        return 0
    if dp[c]:
        return dp[c]
    sum = solve(c//2) + solve(c//3) + solve(c//4)
    if sum > c:
        dp[c] = sum
    else:
        dp[c] = c
    return dp[c]

while True:
    try:
        c = int(input())
        print(solve(c))
    except:
        break

