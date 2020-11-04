
def num_spell(num,out,spell_dict,i):
	if i == len(num):
		return out

	out += spell_dict[int(num[i])]
	out += ' '
	return num_spell(num,out,spell_dict,i+1)




num = 7976016059
spell_dict = {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
out = ''
ans = num_spell(str(num),out,spell_dict,0)
print(ans)