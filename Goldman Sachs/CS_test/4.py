if __name__ == "__main__":
    n,m = list(map(int,input().strip().split()))
    p = list(map(float,input().strip().split()))
    x = list(map(float,input().strip().split()))
    y = list(map(float,input().strip().split()))

    dp = [0.00 for _ in range(n)]
    print(dp)

    for i in range(n):  
        ans = p[i]*x[i] - (1 - p[i])*y[i]
        if ans < 0:
            continue
        else:
            dp[i] = "{0:.2f}".format(ans)
    dp = sorted(dp,reverse=True)
    sum = 0.0
    for i in range(m):  
        sum += dp[i] 
    print(dp)   
    print("{0:.2f}".format(sum))