
def string_int(num,i):
	if i==len(num):
		return 0

	small_ans = string_int(num,i+1)
	return small_ans*10 + int(num[len(num)-i-1])



num = "123"
ans = string_int(num,0)
print(ans)