class Solution:
	# @param A a list of integers
	# @param m an integer, length of A
	# @param B a list of integers
	# @param n an integer, length of B
	# @return nothing
	def merge(self, A, m, B, n):
		for i in range(m+n-1,-1,-1):
			if m==0 or (n>0 and A[m-1]<B[n-1]):
				A[i]=B[n-1]
				n -= 1
			else:
				A[i]=A[m-1]
				m -= 1
		return A
