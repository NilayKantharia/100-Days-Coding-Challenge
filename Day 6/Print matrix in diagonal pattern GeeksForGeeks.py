class Solution:
    def matrixDiagonally(self,mat):
        res=[]
        i=0
        j=0
        n=len(mat)
        m=len(mat[0])
        d=-1
        while i<n and j<m:
            si=j
            sj=i
            if d==-1:
                while i>=si and j<=sj:
                    res.append(mat[i][j])
                    i-=1
                    j+=1
                i+=1
                j-=1
            elif d==1:
                while i<=si and j>=sj:
                    res.append(mat[i][j])
                    i+=1
                    j-=1
                i-=1
                j+=1
            if d==1:
                if i==n-1:
                    j+=1
                else:
                    i+=1
                d=(-1)
            elif d==-1:
                if j==n-1:
                    i+=1
                else:
                    j+=1
                d=1
        return res

