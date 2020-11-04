
def sub_string(str_input,out,i,j):
	if i == len(str_input):
		out = out[:j]
		print(''.join(out))
		return


	out[j] = str_input[i]

	sub_string(str_input,out,i+1,j+1)
	sub_string(str_input,out,i+1,j)





str_input = "abc"
out = ['']*(len(str_input))
sub_string(str_input,out,0,0)