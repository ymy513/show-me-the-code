import uuid
import MySQLdb

def CreateCode(count):
	code_list = []
	for i in xrange(count):
		code = str(uuid.uuid4()).replace('-','').upper()
		if not code in code_list:
			code_list.append(code)

	return code_list

def Write2MySQL(code_list):
	# connect to database
	db = MySQLdb.connect("localhost","test")