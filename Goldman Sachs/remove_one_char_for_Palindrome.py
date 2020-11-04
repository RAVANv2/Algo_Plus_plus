

def sub_string_isPalindrome(str_in,left,right):
	while left < right:
		if str_in[left] != str_in[right]:
			left +=1
			right -=1
		return False
	return True


def is_palindrome_possible(str_in,count):
	left = 0
	right = len(str_in) - 1 

	while left < right: 

		if str_in[left] == str_in[right]:
			left += 1
			right -= 1

		else:

			if sub_string_isPalindrome(str_in,left+1,right):
				return left

			if sub_string_isPalindrome(str_in,left,right+1):
				return right

			return -1
	return -2


if __name__ == "__main__":
	str_in = "aaba"
	idx = is_palindrome_possible(str_in,0)
	print(idx)