class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        zeros,ones=0,0
        for i in s:
            if i=='0':
                zeros+=1
            else:
                ones+=1
        for i in range(ones-1):
            res+='1'
        for i in range(zeros):
            res+='0'
        res+='1'
        return res

        
