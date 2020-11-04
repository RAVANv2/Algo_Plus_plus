
def find_cost(n,max_weight,weights,cost,dp):

	if n==0 or max_weight == 0:
		return 0

	if dp[n]!=0:
		return dp[n]

	inc = ex = float('-inf')

	if max_weight >= weights[n-1]:
		inc = cost[n-1] + find_cost(n-1,max_weight-weights[-1],weights,cost,dp)
	ex = find_cost(n-1,max_weight,weights,cost,dp)

	dp[n] = max(inc,ex)
	return dp[n]


weights = [1,2,3,5]
cost = [40,20,30,100]
max_weight = 7
dp = [0]*(len(weights)+1)
print(find_cost(len(weights),max_weight,weights,cost,dp))
print(dp)