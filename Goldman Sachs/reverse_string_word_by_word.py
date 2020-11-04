
def reverse_str(str_int,start,end):
	while start < end:
		temp = str_int[start]
		str_int[start] = str_int[end]
		str_int[end] = temp
		start += 1
		end -= 1
	return str_int


if __name__ == "__main__":
	str_int = ['p','a','r','s','r']
	ans = reverse_str(str_int,0,len(str_int)-1)
	print(''.join(ans))