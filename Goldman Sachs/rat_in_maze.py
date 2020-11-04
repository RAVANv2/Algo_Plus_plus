
N = 4
def check(maze,i,j):
	if i>=0 and i<N and j>=0 and j<N and maze[i][j]==1:
		return True
	return False

def path_find(maze,sol,i,j,cnt):
	if i==N-1 and j==N-1 and maze[i][j]==1:
		sol[i][j] = 1
		for k in range(N):
			for l in range(N):
				print(sol[k][l],end=' ')
			print()
		print("*"*30)
		cnt[0] +=1
		return True

	if check(maze,i,j):
		sol[i][j] = 1

		vert = path_find(maze,sol,i+1,j,cnt)
		hori = path_find(maze,sol,i,j+1,cnt)
		
		if vert or hori:
			return True
		
		sol[i][j] = 0

		return False

	return False

if __name__ == "__main__":
	maze = [ [1,'X','X','X'],
			 [1,1,'X',1],
			 ['X',1,1,1],
			 [1,1,1,1] ]
	cnt = [0]
	sol = [[0 for _ in range(N)] for _ in range(N)]
	print(path_find(maze,sol,0,0,cnt))
	print(cnt)