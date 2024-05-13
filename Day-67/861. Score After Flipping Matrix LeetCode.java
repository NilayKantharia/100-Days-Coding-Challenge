class Solution {
    public int matrixScore(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int res = rows * (int)Math.pow(2, cols - 1);
        
        for(int j = 1; j < cols; j++){
            int count = 0;
            for (int i = 0; i < rows; i++){
                if (grid[i][j] != grid[i][0]){
                    count++;
                }
            }
            count = Math.max(count, rows - count);
            res += count * (int)Math.pow(2, cols - j - 1);
        }
        return res;
    }
}
