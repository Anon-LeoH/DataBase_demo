from cachePage import CachePage

MAX_PAGE_SIZE = 1024

class FirstLevelCache(object):
    def __init__(self, mark):
        self.direction = mark.direction
        self.args = mark.args
        self.page = CachePage(MAX_PAGE_SIZE, self.direction)
        self.page.readFile()

    def searchByID(self, ID):
        return self.page.searchByID(ID)

    def searchByArgs(self, args):
        return self.page.searchByArgs(args)

    def findAll(self):
        return self.page.findAll()

    def changeByMark(self, newMark):
        self.direction = newMark.direction
        self.args = newMark.args
        self.page.direction = self.direction
        self.page.readFile()

    def changeByPage(self, page):
        self.page = page
        self.page.readFile()

