class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        decHappiness = 0
        happiness.sort()
        maxSum = 0
        while k:
            maxSum += happiness.pop() - decHappiness if (happiness[-1] - decHappiness) > 0 else 0
            decHappiness += 1
            k -= 1
        return maxSum
