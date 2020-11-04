
def power(a,n):
	if n==0:
		return 1

	ans = a*power(a,n-1)
	return ans


def fast_power(a,n):
	if n==0:
		return 1

	sub_ans = fast_power(a,n//2)
	sub_ans *= sub_ans

	if n&1:
		return sub_ans*a
	return sub_ans


a = 5
n = 3
print(power(a,n))
print(fast_power(a,n))