

decode = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



def count(num):
	cnt = 0
	while num > 26:
		cnt+=1
		num -= 26
	return num,cnt

num = int("702")
cnt = 0
out = ''
if num > 26:
	num,cnt = count(num)
	out += decode[num]
	while cnt > 26:
		num,cnt = count(cnt)
		out += decode[num]
	out += decode[cnt]
	print(out[::-1])
else:
	print(decode[num])


