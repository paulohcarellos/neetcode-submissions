class Solution:
	def isValid(self, s: str) -> bool:
		if len(s) & 1:
			return False
	
		pairs = {'(': ')', '[': ']', '{': '}'}
		stack = []
		push = stack.append
		pop = stack.pop
	
		for c in s:
			if c in pairs:
				push(pairs[c])
			elif not stack or pop() != c:
				return False
	
		return not stack