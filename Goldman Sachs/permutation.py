
def permutation(string,i,s):
	if i == len(string):
		print(''.join(string))
		return

	for k in range(len(string)):
		string[i], string[k] = string[k], string[i]
		permutation(string,i+1,s)
		string[i], string[k] = string[k], string[i]

string = list("abc")
s = set()
permutation(string,0,s)
print(s)