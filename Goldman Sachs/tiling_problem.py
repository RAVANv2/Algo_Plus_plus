


def ways(n,dp):

	if n <= 4:
		return 1

	if dp[n]!=0:
		return dp[n]

	hori = ways(n-4,dp)
	vert = ways(n-1,dp)
	dp[n] = hori+vert
	return dp[n]




n = 8
dp = [0]*(n+1)
print(ways(n,dp))
print(dp)