class Solution:
    def largestSubsquare(self, n, a):
        
        if n==1:
            return 1
            
        
        byr=[[0 for i in range(n)] for j in range(n)]
        byc=[[0 for i in range(n)] for j in range(n)]
        
        for i in range(n):
            r=0
            for j in range(n):
                if a[i][j]=='X':
                    r+=1
                else:
                    r=0
                byr[i][j]=r
        
        for j in range(n):
            c=0
            for i in range(n):
                if a[i][j]=='X':
                    c+=1
                else:
                    c=0
                byc[i][j]=c
                
        res=0
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                s=min(byr[i][j],byc[i][j])
                while s>res:
                    if byr[i-s+1][j]>=s and byc[i][j-s+1]>=s:
                        res=s
                    else:
                        s-=1
        return res
