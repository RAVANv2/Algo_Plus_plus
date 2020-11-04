

def generate_string(num,i,phone_dict,out):
	if i == len(num):
		print(''.join(out))
		return

	digit = int(num[i])
	for j in range(len(phone_dict[digit])):
		out[i] = phone_dict[digit][j]
		generate_string(num,i+1,phone_dict,out)



num = str(34)
phone_dict = {0:'',1:'',2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
out = ['']*(len(str(num)))
generate_string(num,0,phone_dict,out)