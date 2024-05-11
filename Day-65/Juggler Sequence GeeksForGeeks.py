import math
class Solution:
    def jugglerSequence(self, n):
        res = []
        prev = n
        res.append(n)
        while(prev != 1):
            if prev % 2 == 1:
                res.append(int(math.sqrt(prev ** 3)))
            else:
                res.append(int(math.sqrt(prev)))
            prev = res[-1]
        return res
