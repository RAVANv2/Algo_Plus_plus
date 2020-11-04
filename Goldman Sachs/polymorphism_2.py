class day:
	def add(self,a:int,b:int)-> int:
		print('1')
		print(a+b)
		return a+b

	def add(self,a:str,b:str)->str:
		print('2')
		print(a+b)
		return a+b


x = day()
x.add(4,5)
x.add('a','b')
