class Solution(object):
    def ispalindrome(self,st):
        return st==st[::-1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if self.ispalindrome(s):
            return s
        lp=[None,0]
        n=len(s)
        for i in range(n):
            for j in range(n-1,i,-1):
                if len(s[i:j+1]) > lp[1]:
                    if self.ispalindrome(s[i:j+1]):
                        lp[0]=s[i:j+1]
                        lp[1]=len(s[i:j+1])
        return lp[0] if lp[0] else s[0]

