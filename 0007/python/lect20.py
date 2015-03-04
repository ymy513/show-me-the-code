class Solution:
	# @return a boolean
	def isValid(self, s):
		dict = {'(':')','[':']','{':'}'}
		stk = []
		for c in s:
			if dict.get(c, None):
				stk.append(c)
			elif len(stk)==0 or dict[stk[-1]]!=c:
				return False
			else:
				stk.pop()
		return True if len(stk)==0 else False
