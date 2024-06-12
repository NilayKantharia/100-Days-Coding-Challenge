class Solution:
    def countNumberswith4(self, n : int) -> int:
        res = 0
        for i in range(n + 1):
            s = str(i)
            for j in s:
                if j == '4':
                    res += 1
                    break
        return res
        
