class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        while s[n-1] == ' ':
            n = n-1
        count = 0
        for i in range(n-1,-1,-1):
            if s[i] == ' ':
                break
            else:
                count += 1
        return count
