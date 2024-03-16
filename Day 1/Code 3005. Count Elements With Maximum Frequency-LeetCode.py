class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        maxn=max(nums)
        c=[0]*(maxn+1)
        count=0
        for i in range(l):
            c[nums[i]]+=1
        cmax=max(c)
        for i in range(maxn+1):
            if c[i]==cmax:
                 count+=c[i]
        if not count:
            return cmax
        else:
            return count 
