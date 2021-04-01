import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


n,a,b,c=map(int,input().split())
z=[0]+[-1e9]*5000
for i in range(1,n+1):
    z[i]=max(z[i-a],z[i-b],z[i-c])+1

print(z[:n])
print(z[n])







