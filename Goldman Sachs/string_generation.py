	
def generate(array,alpha,i,j,out):

	if i == len(array):
		out = out[:j]
		print(''.join(out))
		return

	out[j] = alpha[int(array[i])]

	generate(array,alpha,i+1,j+1,out)

	if i!=len(array)-1 and int(array[i]+array[i+1]) <= 26:
		out[j] = alpha[int(array[i]+array[i+1])]
		generate(array,alpha,i+2,j+1,out)


alpha = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
array = "1212"
out = ['']*(len(array))
generate(array,alpha,0,0,out)