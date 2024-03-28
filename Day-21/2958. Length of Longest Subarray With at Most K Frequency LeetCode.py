class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashMap = {}
        l = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] in hashMap:
                hashMap[nums[r]] += 1
                while hashMap[nums[r]] > k:
                    hashMap[nums[l]] -= 1
                    l += 1
            else:
                hashMap[nums[r]] = 1
            res = max(res,r-l+1)
        return res
