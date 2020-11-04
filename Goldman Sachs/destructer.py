class A:
	def __init__(self):
		print("Init Method")

	def __del__(self):
		print("Destructer Called")

a = A()
print("hii")