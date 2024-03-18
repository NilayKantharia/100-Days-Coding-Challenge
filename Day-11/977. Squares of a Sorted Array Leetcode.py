class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        n=len(nums)
        for i in range(n):
            res.append(nums[i]*nums[i])
        res.sort()
        return res
