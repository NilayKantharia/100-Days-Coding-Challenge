class Solution:
    def minRow(self,n,m,a):
        minOne = 1000
        currIdx = 0
        for i in range(n):
            count = 0
            for j in range(m):
                if a[i][j] == 1:
                    count += 1
            if count < minOne:
                minOne = count
                currIdx = i
        return currIdx + 1
