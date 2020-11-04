class Student:
	def __init__(self,name,marks):
		self.__name = name
		self.__marks = marks

	def access(self):
		print(self.__name,self.__marks) 
		return 

obj = Student('Harsh',100)
print(obj._Student__name)