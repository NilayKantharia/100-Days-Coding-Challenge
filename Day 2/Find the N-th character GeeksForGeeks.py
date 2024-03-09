class Solution:
    def nthCharacter(self, s, r, n):
        if r==0: return s[n]
        c=self.nthCharacter(s,r-1,n//2)
        if(n%2==1):
            if c=='0':
                return '1'
            return '0'
        else:
            if c=='0':
                return '0'
            return '1'
                
            
