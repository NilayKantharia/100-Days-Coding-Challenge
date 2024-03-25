class Solution:
    def helper(self, n, current, res, ones, zeros):
        if zeros > ones:
            return
        if len(current) == n:
            res.append(current)
            return
        self.helper(n, current + '1', res, ones+1, zeros)
        self.helper(n, current + '0', res, ones, zeros+1)
        
        
	def NBitBinary(self, n):
		ones = 0; zeros = 0; current = ''; res = []
		self.helper(n, current, res, ones, zeros)
    	return res
