class Solution(object):
    def wonderfulSubstrings(self, word):
        count = [0] * 1024
        res = 0
        prex = 0
        count[prex] = 1
        
        for c in word:
            ind = ord(c) - ord('a')
            prex ^= 1 << ind
            res += count[prex]
            for i in range(10):
                res += count[prex ^ (1 << i)]
            count[prex] += 1
        
        return res
