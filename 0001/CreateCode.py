#!/usr/bin/env python
import uuid

def CreateCode(count):
	code_list = []
	for i in xrange(count):
		code = str(uuid.uuid4()).replace('-','').upper()
		if not code in code_list:
			code_list.append(code)

	return code_list

if __name__ == "__main__":
	code_list = CreateCode(200)
	for code in code_list:
		print code+'\n'