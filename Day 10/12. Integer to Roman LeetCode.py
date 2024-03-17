class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        hashMap=[[1,'I'],[4,'IV'],[5,'V'],[9,'IX'],[10,'X'],[40,'XL'],[50,'L'],[90,'XC'],[100,'C'],
        [400,'CD'],[500,'D'],[900,'CM'],[1000,'M']]

        res=""
        n=len(hashMap)
        for i in range(n-1,-1,-1):
            if num//hashMap[i][0]:
                count = num//hashMap[i][0]
                res+=hashMap[i][1]*count
                num=num%hashMap[i][0]
        return res



        
