import uuid

ErrorMsg = "******\n" + "Error occur in file item.py\n" + "Please recheck your operation!\n" + "*******\n"

class item(object):
	def __init__(self, valDic):
		self._id = uuid.uuid1()
		valDic.update({"id": self._id})
		self.vals = valDic
	
	def __str__(self):
		return str(self._id) + ": " + str(self.vals)

	def __eq__(self, val):
		if isinstance(val, item):
			if val._id == self._id:
				return True
			else:
				return False
		elif isinstance(val, dict):
			val.update({"id": self._id})
			if val == self.vals:
				return True
			else:
				return False
		elif isinstance(val, str):
			tmp = None
			try:
				tmp = eval(val)
			except IOError, TypeError, NameError, SyntaxError:
				print ErrorMsg
				return False
			if tmp != None:
				tmp.update({"id": self._id})
				if tmp == self.vals:
					return True
				else:
					return False
		else:
			print "args type error occur!\n"
			return False
	
	def __le__(self, val):
		if val == self:
			return True
		if isinstance(val, item):
			val = val.vals
		elif isinstance(val, str):
			tmp = None
			try:
				tmp = eval(val)
			except IOError, TypeError, NameError, SyntaxError:
				print ErrorMsg
				return False
			if tmp:
				val = tmp
			else:
				return False
		if isinstance(val, dict):
			for key in val:
				if not self.vals[key]:
					return False
				if not val[key] == self.vals[key]:
					return False
			return True
		else:
			print "args type error occur!\n"
			return False

