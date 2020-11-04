
def replace_pi(string,i,string_dict):

	if i == len(string):
		return

	if string[i] + string[i+1] == 'pi':
		string_dict['out'] += "3.14"
		replace_pi(string,i+2,string_dict)
	else:
		string_dict['out'] += string[i]
		replace_pi(string,i+1,string_dict)



string = "xpighpilmpipi"
string_dict = dict()
string_dict['out'] = ''
replace_pi(string,0,string_dict)
print(string_dict['out'])

