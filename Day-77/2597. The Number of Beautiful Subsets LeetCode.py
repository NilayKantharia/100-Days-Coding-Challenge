class Solution:
    def subSets(self, i, count, k, nums, n):
        if i == n:
            return 1
        res = self.subSets(i + 1, count, k, nums, n)
        if not count[nums[i] + k] and not count[nums[i] - k]:
            count[nums[i]] += 1
            res += self.subSets(i + 1, count, k, nums, n)
            count[nums[i]] -= 1
        return res

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = defaultdict(int)
        return self.subSets(0, count, k, nums, n) - 1
