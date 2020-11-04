class parent:
	def __init__(self,fatherName):
		self.fatherName = fatherName

class child_A(parent):
	def __init__(self,fatherName,sonName):
		self.sonName = sonName
		super().__init__(fatherName)

	def print_family(self):
		print(f"Father: {self.fatherName} \nSon: {self.sonName}")
		

class child_B(parent):
	def __init__(self,fatherName,motherName):
		self.motherName = motherName
		super().__init__(fatherName)

	def print_family(self):
		print(f"Father: {self.fatherName} \nMother: {self.motherName}")

obj_A = child_A("Sukhbir","Harsh")
obj_A.print_family()

print()

obj_B = child_B("Sukhbir","Lalita")
obj_B.print_family()
