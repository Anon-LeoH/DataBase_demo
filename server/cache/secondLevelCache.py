from cachePage import CachePage

MAX_PAGE_SIZE = 1024

class SecondLevelCache(object):
    def __init__(self, marks = []):
        self.directions = [item.direction for item in marks]
        self.argsList = [item.args for item in marks]
        self.pages = []
        for i in xrange(len(marks)):
            self.pages.append(CachePage(MAX_PAGE_SIZE, self.directions[i]))

    def getAPage(self):
        rlt = self.pages[0]
        self.pages.remove(self.pages[0])
        self.directions.remove(self.directions[0])
        self.argsList.remove(self.argsList[0])
        return rlt

    def getPageByArgs(self, args):
        rlt == None
        for page in self.pages:
            if page.args == args:
                rlt = page
                break
        if rlt:
            self.pages.remove(rlt)
            self.directions.remove(rlt.direction)
            self.argsList.remove(rlt.args)
        return rlt

    def insertPageByMark(self, mark):
        tmp = CachePage(MAX_PAGE_SIZE, mark.direction)
        self.directions.append(mark.direction)
        self.argsList.append(mark.args)
        self.pages.append(tmp)

    def insertPageByPage(self, page):
        self.directions.append(page.direction)
        self.argsList.append(page.args)
        self.pages.append(page)

    def clear(self):
        self.directions = []
        self.argsList = []
        self.pages = []




