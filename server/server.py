from flask import Flask
from router import Router
app = Flask(__name__)

router = Router(app)

@app.route('/insert/<colName>/<data>')
def insert(colName, data):
	if request.method == 'POST':
		try:
			data = eval(data)
		except:
			return "inlegal option!"
		if not isinstance(data, dict):
			return "Type Error!"
		rlt = router.insert(colName, data)
		if rlt:
			return "Succeed!"
		else:
			return "Failed"
	else:
		return "Request reject!"

@app.route('/removeByID/<colName>/<ID>')
def removeByID(colName. ID):
	if request.method == "POST":
		rlt = router.removeByID(colName, ID)
		if rlt:
			return "Succeed"
		else:
			return "Failed"
	else:
		return "Request reject!"

@app.route('/removeByArgs/<colName>/<args>')
def removeByArgs(colName, args):
	if request.method == "POST":
		try:
			args = eval(args)
		except:
			return "inlegal option!"
		if not isinstance(args, dict):
			return "Type Error!"
		rlt = router.removeByArgs(colName, args)
		if rlt:
			return "Succeed"
		else:
			return "Failed"
	else:
		return "Request reject!"

@app.route('/updateByID/<colName>/<ID>/<newArgs>')
def updateByID(colName, ID, newArgs):
	if request.method == "POST":
		rlt = router.updateByID(colName, ID, newArgs)
		if rlt:
			return "Succeed"
		else:
			return "Failed"
	else:
		return "Request reject!"

@app.route('/updateByArgs/<colName>/<args>')
def updateByArgs(colName, args):
	if request.method == "POST":
		try:
			args = eval(args)
		except:
			return "inlegal option!"
		if not isinstance(args, list):
			return "Type Error!"
		if not isinstance(args[0], dict):
			return "Type Error!"
		if not isinstance(args[1], dict):
			return "Type Error!"
		rlt = router.updateByArgs(colName, args[0], args[1])
		if rlt:
			return "Succeed"
		else:
			return "Failed"
	else:
		return "Request reject!"

@app.route('/searchByID/<colName>/<ID>')
def serachByID(colName. ID):
	if request.method == "POST":
		rlt = router.searchByID(colName, ID)
		if rlt:
			return str(rlt)
		else:
			return "Failed"
	else:
		return "Request reject!"

@app.route('/searchByArgs/<colName>/<args>')
def searchByArgs(colName, args):
	if request.method == "POST":
		try:
			args = eval(args)
		except:
			return "inlegal option!"
		if not isinstance(args, dict):
			return "Type Error!"
		rlt = router.searchByArgs(colName, args)
		if rlt:
			return rlt
		else:
			return "Failed"
	else:
		return "Request reject!"

