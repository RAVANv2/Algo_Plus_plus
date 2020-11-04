class A:
	def m(self):
		print("Class A")

class B:
	def m(self):
		super().m()
		print("Class B")

class C(B,A):
	def m(self):
		super().m()
		print("Class C")


obj = C()
obj.m()