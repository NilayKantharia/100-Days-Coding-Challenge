class Solution:
    def dfs(self, row, col, grid):
        if (row >= self.ROW or 
            col >= self.COL or
            row < 0 or
            col < 0 or
            grid[row][col] == 0):
            return 1
        if grid[row][col] == -1:
            return 0
        grid[row][col] = -1
        perimeter = self.dfs(row + 1, col, grid)
        perimeter += self.dfs(row, col + 1, grid)
        perimeter += self.dfs(row - 1, col, grid)
        perimeter += self.dfs(row, col - 1, grid)
        return perimeter

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.ROW = len(grid)
        self.COL = len(grid[0])
        for i in range(self.ROW):
            for j in range(self.COL):
                if grid[i][j]:
                    return self.dfs(i, j, grid)

