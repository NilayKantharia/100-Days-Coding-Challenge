class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeros=0
        ones=0
        hashMap={}
        hashMap[0]=-1
        res=0
        n=len(nums)

        for i in range(n):
            if nums[i]==0:
                zeros+=1
            else:
                ones+=1
            if ones-zeros in hashMap:
                res=max(res,i-hashMap[ones-zeros])
            else:
                hashMap[ones-zeros]=i
                
        return res
        
        
