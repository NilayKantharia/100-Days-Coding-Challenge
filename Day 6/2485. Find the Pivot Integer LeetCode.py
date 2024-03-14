class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        for i in range(n//2,n):
            sum1=i*(i+1)//2
            sum2=(n*(n+1)//2)-sum1+i
            if sum1==sum2:
                return i
        return -1
        
