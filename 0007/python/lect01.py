class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		dict = {}
		for i in range(len(num)):
			if dict.get(target-num[i],None)==None:
				dict[num[i]]=i
			else:
				return (dict[target-num[i]]+1,i+1)