class Solution:
    def dfs(self, i, total, nums, n):
        if i == n:
            return total
        return self.dfs(i + 1, total ^ nums[i], nums, n) + self.dfs(i + 1, total, nums, n)

        
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.dfs(0, 0, nums, len(nums))
        
