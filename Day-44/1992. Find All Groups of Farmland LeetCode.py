class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n = len(land)
        m = len(land[0])

        res = []

        for row in range(n):
            for col in range(m):
                if land[row][col]:
                    r2 = row
                    while r2 < n and land[r2][col]:
                        c2 = col
                        while c2 < m and land[r2][c2]:
                            land[r2][c2] = 0
                            c2 += 1
                        r2 += 1
                    res.append([row, col, r2 - 1 , c2 - 1])

        return res
