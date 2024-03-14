class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows>=len(s) or numRows==1:
            return s
        arr=[[] for i in range(numRows)]
        i=0
        d=-1
        n=len(s)
        for j in s:
            arr[i].append(j)
            if i==0:
                d=1
            elif i==numRows-1:
                d=-1
            i+=d
        for i in range(numRows):
            arr[i]=''.join(arr[i])
        return ''.join(arr)
