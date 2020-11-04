def permutation(ch,i,ans):
	if i == len(ch):
		out = ''.join(ch)
		ans.append(out)
		# print(ans)2
		return

	for k in range(i,len(ch)):
		ch[k] , ch[i] = ch[i] , ch[k]
		permutation(ch,i+1,ans)
		ch[k] , ch[i] = ch[i] , ch[k]



def main():
	ch = ["a","b","c"]
	ans = []
	permutation(ch,0,ans)
	print(ans)

main()