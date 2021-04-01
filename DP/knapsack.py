
def cal(val,weight,w,n,dp):
    if n ==0  or w==0:
        return 0

    if weight[n-1] > w:
        return cal(val,weight,w,n,dp)

    if dp[n]!=-1:
        return dp[n]

    score = max(val[n-1] + cal(val, weight, w-weight[n-1],n-1,dp), cal(val,weight,w,n-1,dp))
    dp[n] = score
    print(dp)
    return dp[n]


val = [60,100,120]
weight = [10,20,30]
w = 50
n = len(val)
dp = [-1 for i in range(n+1)]
print(cal(val,weight,w,n,dp))