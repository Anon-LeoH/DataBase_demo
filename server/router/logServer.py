import time
import uuid

class log(object):
	def __init__(self, ID, TYPE, contentID, Content, File):
		self.tm = time.time()
		self.ID = ID
		self.TYPE = TYPE
		self.contentID = contentID
		self.Content = Content
		self.File = File
		self msg = "Operation" + str(self.ID) + ": "
		self.msg += str(TYPE) + " data " + str(contentID)
		self.msg += " to file " + str(self.File)
		self.msg += "\n" + "new content is: " + str(self.Content)
		self.msg += "\n" + "Timed: " + str(self.tm)
	
	def __str_ (self):
		return self.msg

class logServer(object):
	def __init__(self, fileDirection, deadTime):
		self.fileDirection = fileDirection
		self.deadTime = deadTime
		self.logPool = []
		self.f = open(fileDirection, "a")
	
	def log(self, TYPE, contentID, Content, File):
		try:
            ID = uuid.uuid1()
		    tmpLog = log(ID, TYPE, contentID, Content, File)
		    self.logPool.append(tmpLog)
		    self.f.write(str(tmpLog) + "\n")
            return True
        except:
            return False
	
	def viewAll(self):
		tmpf = open(self.fileDirection, "r")
		print "********************"
		counter = 0
		for line in tmpf.xreadlines():
			if counter >= 30:
				op = raw_input("y to continue: ")
				if op != "y":
					break
				else:
					counter = 0
			print line
			counter += 1
	
# Additional operations still under development.

