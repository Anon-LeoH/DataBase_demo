from router import router
from taskQueue import taskQueue
from cache import *
from logServer import logServer

defaultVals = {
		          "log_file": "./log.log",
				  "config_file": "./config.cfg"
		      }

def getRouter(_id, argvs):
	taskQueue_length = 50
	deadTime = 10
	fcNum = 1
	scNum = 3
	logType = "ALL"
	try:
		f = open()

