class Solution:
	def countPairs(self, mat1, mat2, n, x):
		# code here
		count=0
        i=0;j=0;p=n-1;q=n-1
        while i<n and p>=0:
            sum=mat1[i][j]+mat2[p][q]
            if sum==x:
                count+=1
                j+=1
                q-=1
            if sum>x:
                q-=1
            if sum<x:
                j+=1
            if q==-1:
                q=n-1
                p-=1
            if j==n:
                j=0
                i+=1
        return count
