class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        for i in range(len(s)):
            num=num << 1
            if s[i] == '1':
                num += 1
        
        count = 0
        while(num > 1):
            if (num%2 == 0):
                num //= 2
            else:
                num += 1
            count += 1
        return count
        
        
