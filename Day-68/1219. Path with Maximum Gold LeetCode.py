class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j, visited):
            if i < 0 or j < 0 or i == rows or j == cols or grid[i][j] == 0 or (i, j) in visited:
                return 0
            visited.add((i, j))
            ans = grid[i][j]
            ans = max(ans, grid[i][j] + dfs(i + 1, j, visited))
            ans = max(ans, grid[i][j] + dfs(i, j + 1, visited))
            ans = max(ans, grid[i][j] + dfs(i - 1, j, visited))
            ans = max(ans, grid[i][j] + dfs(i, j - 1, visited))
            visited.remove((i, j))
            return ans

        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j, set()))
        return res
