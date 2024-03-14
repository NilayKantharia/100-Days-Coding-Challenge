class Solution(object):

    def atmost(self,nums,k):
        sum=0
        end=0
        st=0
        count=0
        while end<len(nums):
            sum+=nums[end]
            end+=1
            while st<end and sum>k:
                sum-=nums[st]
                st+=1
            count+=end-st
        return count


    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        return self.atmost(nums,goal)-self.atmost(nums,goal-1)

