from collection import Item
from tool import *
from copy import deepcopy as dc

class cachePage(object):
	def __init__(self, size, direction):
		self.max_size = size
		self.direction = direction
        self.overflow = False
	
	def readFile(self):
        self.data = readFile(self.direction)
        if self.data == None:
            sefl.overflow = True
            self.data = readFileSafe(self.direction, self.max_size)

    def searchByID(self, ID):
        if ID in self.data:
            return self.data[ID]
        else:
            return None

    def searchByArgs(self, args):
        rlt = []
        if not isinstance(args, dict):
            return None

        for item in self.data:
            for key in args:
                if not (key in item.vals and args[key] == self.vals[key]):
                    break
            else:
                rlt.append(item)

        if rlt == []:
            rlt = None

        return rlt

    def findAll(self):
        rlt = dc(self.data)
        return rlt


