from item import Item
from tool import *
import os

class Page(object):
    def __init__(self, parent, key, args):
        self.args = args
        self.key = key
        self.parent = parent
        self.name = str(args).replace("{", "").replace("}", "").replace(":", ",").replace('"', "!").replace(" ", "")
        self.direction = self.parent.direction + "/" + self.name
        self.mark = Marker(self.direction, self.args)
        self.parent.marks[self.key] = self.mark
        os.mkdir(self.direction)

    def mount(self):
        self.parent.cache.changeByMark(self.mark)

    def insert(self, item):
        pass

    def remove(self, item):
        pass

    def update(self, item, args):
        pass

    def searchByID(self, ID):
        pass

    def searchByArgs(self, args):
        pass

        
