    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        mid = n//2
        res = 0
        res += k - nums[mid]
        if k > nums[mid]:
            i = mid + 1
            while i < n and nums[i] < k:
                res += k - nums[i]
                i += 1
        else:
            i = mid - 1
            while i >= 0 and nums[i] > k :
                res += k - nums[i]
                i -= 1
        return abs(res)
