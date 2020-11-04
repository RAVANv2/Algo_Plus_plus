
def lsc_recursion(s1,s2,m,n,string):
	if m == 0 or n == 0:
		return 0

	elif s1[m-1] == s2[n-1]:
		if s1[m-1] not in string:
			string.append(s1[m-1])
		return 1 + lsc_recursion(s1,s2,m-1,n-1,string)
	else:
		return max(lsc_recursion(s1,s2,m-1,n,string),lsc_recursion(s1,s2,m,n-1,string))


def lcs_dp(s1,s2):
	m = len(s1)
	n = len(s2)

	dp = [[None for _ in range(n+1)] for _ in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				dp[i][j] = 0
			elif s1[i-1] == s2[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i][j-1],dp[i-1][j])

	for i in range(m+1):
		for j in range(n+1):
			print(dp[i][j],end=' ')
		print()

	return dp[m][n]


if __name__ == "__main__":
	s1 = "XXTAMB"
	s2 = "PQXSTZABU"
	# ans = "XTAB"
	string = []
	print(lsc_recursion(s1,s2,len(s1),len(s2),string))
	print(''.join(string))

	print(lcs_dp(s1,s2))