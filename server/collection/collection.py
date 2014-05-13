from page import *
from deliverTree import *
from dbConfig import *
from copy import deepcopy as dc
import uuid
import os

class Collection(object):
	def __init__(self, name, principles): #still need another agrvs
		self.principles = principles
        self.name = name
        self.direction = dbDirection + "/" + self.name
        if os.path.exists(self.direction):
            raise IOError
            return
        os.mkdir(self.direction)
        self.pages = {}
        self.ID = uuid.uuid1()

    def getKey(self, item):
        args = {}
        for key in self.principles:
            if key in item.vals:
                args.update({key: item.vals[key]})
            else:
                args.update({key: None})
        key = str(args)
        return key

    def insert(self, item):
        key = self.getKey(item)
        if key in self.pages:
            self.pages[key].insert(item)
        else:
            self.pages[key] = Page(self, args)
            self.pages[key].insert(item)

    def update(self, item, args):
        for key in args:
            if key in self.principles:
                break
        else:
            key = self.getKey(item):
            self.pages[key].update(item, args)
            return
        tmp = dc(item)
        key = self.getKey(item)
        self.pages[key].remove(item)
        for key in args:
            tmp.vals[key] = args[key]
        self.insert(tmp)

    def searchByID(self, ID):
        for key in self.pages:
            tmp = self.pages[key].searchByID(ID)
            if tmp:
                return tmp
        return None

    def searchByArgs(self, args):
        tmp = {}
        for key in self.principles:
            if key in args:
                tmp.update({key: args[key]})
            else:
                tmp.update({key: None})
        key = str(tmp)
        if key in self.pages:
            return self.pages[key].searchByArgs(args)
        else:
            return None

    def remove(self, item):
        key = self.getKey(item)
        self.pages[key].remove(item)


        

