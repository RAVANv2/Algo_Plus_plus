class CS:
	cse = 'abc'
	def __init__(self):
		self.new = "x"
		
	def fun(self):
		self.cse = "ab"
		print(self.cse)

x = CS()
print(x.cse)
print(x.new)
x.fun()