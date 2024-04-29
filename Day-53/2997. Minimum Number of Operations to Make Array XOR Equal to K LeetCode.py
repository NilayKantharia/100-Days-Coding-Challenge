class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        count = 0
        for i in nums:
            res ^= i
        while k or res:
            if k % 2 != res % 2:
                count += 1
            k //= 2
            res //= 2
        return count 
