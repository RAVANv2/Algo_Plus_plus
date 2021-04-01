word1 = "horse"
word2 = "ros"

def minDistance(x,y):

    dp =[[x for x in range(len(x)+1)] for y in range(len(y)+1)]

    for i in range(1,len(y)+1):
        dp[i][0] = dp[i-1][0]+1

    for row in range(1,len(y)+1):
        for col in range(1,len(x)+1):
            if x[col-1] == y[row-1]:
                dp[row][col] = dp[row-1][col-1]
            else:
                dp[row][col] = 1 + min(dp[row-1][col-1],dp[row-1][col],dp[row][col-1])

    for i in range(len(y)+1):
        for j in range(len(x)+1):
            print(dp[i][j],end=' ')
        print()

    print(dp[-1][-1])


minDistance(word1,word2)
