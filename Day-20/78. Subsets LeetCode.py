class Solution:
    def findSubSets(self, nums, i, n, res, final):
        if i == n:
            final.append(res.copy())
            return
        self.findSubSets(nums, i+1, n, res, final)
        res.append(nums[i])
        self.findSubSets(nums, i+1, n, res, final)
        res.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(nums)
        final = []
        self.findSubSets(nums, i, n, res, final)
        return final
        
