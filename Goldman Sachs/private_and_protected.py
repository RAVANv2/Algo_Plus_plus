class india:

	def __init__(self,state):
		self._state = state
		print("init")

	def convert(self):
		self.state = "jaipur"
		print(self.state)

class japan(india):
	def __init__(self,state):
		super().__init__(state)
	

	def access_private(self):
		self.state = "india"
		print(self.state)

obj = japan("raj")
obj.access_private()
