class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        delta = [(n ^ k) - n for n in nums]
        delta.sort(reverse = True)
        res = sum(nums)

        for i in range(0, len(nums) - 1, 2):
            deltaPath = delta[i] + delta[i + 1]
            if deltaPath <= 0:
                break
            res += deltaPath
        return res 
        
