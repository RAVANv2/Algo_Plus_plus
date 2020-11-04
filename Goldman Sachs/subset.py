def generate_string(in_str,out,i,j):

	if i==len(in_str):
		out = out[:j]
		print(''.join(out))
		return

	out[j] = in_str[i]

	generate_string(in_str,out,i+1,j+1)
	generate_string(in_str,out,i+1,j)





in_str = "abc"
out = ['']*(len(in_str))
generate_string(in_str,out,0,0)