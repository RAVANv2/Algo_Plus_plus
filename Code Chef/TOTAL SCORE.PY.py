

t = int(input())

while t:

    t -= 1
    N,K = list(map(int,input().strip().split()))
    A = list(map(int,input().strip().split()))

    for _ in range(N):
        s = input().strip()
        mark = 0
        for i in range(len(s)):
            if s[i]=='0':
                mark += 0
            else:
                mark += A[i]
        print(mark)