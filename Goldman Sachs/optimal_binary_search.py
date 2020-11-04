

def possible_string(n):
	dp = [0]*(n+1)
	dp[0] = 1
	dp[1] = 2

	for i in range(2,n+1):
		dp[i] = dp[i-1] + dp[i-2]

	print(dp)
	return dp[n]


n = 11
print(possible_string(n))