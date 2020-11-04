from collections import OrderedDict

class LRU:
	def __init__(self,capacity):
		self.cache = OrderedDict()
		self.capacity = capacity

	def put(self,key,value):
		self.cache[key] = value
		self.cache.move_to_end(key)

		if len(self.cache) > self.capacity:
			self.cache.popitem(last=False)

	def get(self,key):
		if key not in self.cache:
			return -1

		else:
			self.cache.move_to_end(key)	
			return self.cache[key]


obj = LRU(2)
obj.put(1,4)
obj.put(2,6)
print(obj.cache)

obj.put(3,6)
print(obj.cache)
obj.get(2)
print(obj.cache)