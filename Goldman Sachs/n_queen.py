
N = 10
def print_board(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j],end=' ')
		print()

def isSafe(board,i,j):
	# If any queen is present in row or not
	for row in range(N):
		if board[row][j] == 'Q':
			return False

	# Chek for both the diagonals
	x = i
	y = j
	while x>=0 and y>=0:
		if board[x][y] == 'Q':
			return False
		x-=1
		y-=1

	x = i
	y = j
	while x>=0 and y<N:
		if board[x][y] == 'Q':
			return False
		x-=1
		y+=1
	return True


def solve_queen(board,i):
	if i==N:
		print_board(board)
		print("*"*30)
		return True
	for j in range(N):

		if isSafe(board,i,j):
			board[i][j] = 'Q'
			isValid = solve_queen(board,i+1)
			if isValid:
				return True
			board[i][j] = 0

	return False
if __name__=="__main__":

	board = [[0 for _ in range(N)] for _ in range(N)]
	print(solve_queen(board,0))