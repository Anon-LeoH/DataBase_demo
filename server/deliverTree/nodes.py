class nodeObejct(object):
	def __init__(self, _id, val):
		self._id = _id
		self.val = val
	
	def getVal(self):
		return self.val

	def __str__(self):
		return str(self.val)

