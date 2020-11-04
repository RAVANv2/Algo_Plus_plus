class queue:
	def __init__(self):
		self.queue = []

	def put(self,item):
		self.queue.append(item)
		return self.queue

	def get(self):
		if not self.queue:
			raise Exception("Your queue is Empty")
		return self.queue.pop(0)

	def print_queue(self):
		if not self.queue:
			raise Exception("Your queue is Empty")

		for i in self.queue:
			print(i,end=' ')

q = queue()
q.put(3)
q.put(4)
q.put(5)
q.put(6)
print(q.put(7))
q.get()
q.print_queue()