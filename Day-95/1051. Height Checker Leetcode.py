class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * 101
        for i in heights:
            count[i] += 1
        
        expected = []

        for i in range(1, 101):
            temp = count[i]
            for j in range(temp):
                expected.append(i)

        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        return res
