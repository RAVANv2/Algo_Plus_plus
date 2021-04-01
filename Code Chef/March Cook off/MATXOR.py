import sys

sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


t = int(input())

while t:
    t -= 1

    n,m,k = list(map(int,input().split()))

    mat = []
    # mat.append(0)
    for j in range(1,m+1):
        mat.append(k+1+j)

    nVal = n
    while n != 1:
        mat.append(mat[-1]+1)
        n -= 1

    print(mat)
    ans = 0
    for idx in range(1,len(mat)+1):
        if idx % 2 and nVal % 2 == 1:
            ans ^= mat[idx-1]
        else:
            ans = mat[0] ^ mat[-1]
            break
    print(ans)
