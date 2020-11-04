
def move(n,src,helper,dest):
	if n==0:
		return

	move(n-1,src,dest,helper)
	print(f"Moving {src} to {dest}")
	move(n-1,helper,src,dest)
	
n = 3
move(n,'A','B','C')