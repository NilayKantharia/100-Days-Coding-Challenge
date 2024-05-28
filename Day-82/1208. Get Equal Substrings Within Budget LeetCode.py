class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        maxL = 0
        currSum = 0
        for r in range(len(s)):    
            currSum += abs(ord(s[r]) - ord(t[r]))
            while currSum > maxCost:
                currSum -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            maxL = max(maxL, r - l + 1)
        return maxL
