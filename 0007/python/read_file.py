import os
'''
Input: filename
Output: content
'''
def read(filename):
	if not os.path.exists(filename):
		print("Error: file not exit: %s" % (filename))
		return None
	if not os.path.isfile(filename):
		print("Error: %s not a filename" %(filename))

	f = open(filename,"r")
	content = f.read()
	f.close()

	return content