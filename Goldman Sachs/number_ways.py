def isSafe(m,n,i,j):
	if i>=0 and i<=m and j>=0 and j<=n:
		return True
	return False


def find_ways(m,n,i,j):
	if i==m or j==n:
		return 1

	if isSafe(m,n,i,j):
		x = find_ways(m,n,i+1,j)
		y = find_ways(m,n,i,j+1)

	return x + y

if __name__ == "__main__":
	m = n = 1
	print(find_ways(m,n,0,0))