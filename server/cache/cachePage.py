from collection import Item
from CtoPython import *

class cachePage(object):
	def __init__(self, size, direction, argvs):
		self.max_size = size
		self.argvs = argvs
		self.direction = direction
		self.data = readFile(self.direction)
	
	def searchByID(self, ID):	
