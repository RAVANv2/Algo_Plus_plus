
def change_string(string):

	try:
		string[1] = 'b'
	except Exception as E:
		print(E)
		return string
	return string[1]

if __name__ == "__main__":
	string = "abc"
	ans = change_string(string)
	print(ans)