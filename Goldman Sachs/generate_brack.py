

def generate_brac(n,j,open_brac,close_brac):

	if j==n*2:
		print(''.join(out))
		return
	
	if open_brac < n:
		out[j] = '('
		generate_brac(n,j+1,open_brac+1,close_brac)
	if close_brac < open_brac:
		out[j] = ')'
		generate_brac(n,j+1,open_brac,close_brac+1)




n = 5
out = ['']*n*2
count_dict = dict()
open_brac = 0
close_brac = 0
generate_brac(n,0,open_brac,close_brac)
