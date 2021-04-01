X = "AGGTAB"
Y = "GXTXAYB"

dp = [[0 for _ in range(len(X)+1)] for _ in range(len(Y)+1)]

for i in range(1,len(Y)+1):
    for j in range(1,len(X)+1):
        if X[j-1] == Y[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

for i in range(len(Y)):
    for j in range(len(X)):
        print(dp[i][j],end=" ")
    print()

print(dp[len(Y)][len(X)])