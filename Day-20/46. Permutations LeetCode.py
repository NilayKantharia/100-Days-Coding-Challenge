class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perm = self.permute(nums)
            for j in perm:
                j.append(n)
            res.extend(perm)
            nums.append(n)
        return res

        
