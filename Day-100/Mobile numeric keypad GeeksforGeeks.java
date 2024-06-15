class Solution {
    public long getCount(int n) {
        if (n == 1) {
            return 10;
        }
 
        int[][] moves = {
            {0, 8},      
            {1, 2, 4},   
            {2, 1, 3, 5},
            {3, 2, 6},   
            {4, 1, 5, 7},
            {5, 2, 4, 6, 8},
            {6, 3, 5, 9},
            {7, 4, 8},
            {8, 5, 7, 9, 0},
            {9, 6, 8}
        };

        long[][] dp = new long[10][n];
 
        for (int digit = 0; digit < 10; digit++) {
            dp[digit][0] = 1;
        }
 
        for (int length = 1; length < n; length++) {
            for (int digit = 0; digit < 10; digit++) {
                dp[digit][length] = 0;
                for (int move : moves[digit]) {
                    dp[digit][length] += dp[move][length - 1];
                }
            }
        }
 
        long totalCount = 0;
        for (int digit = 0; digit < 10; digit++) {
            totalCount += dp[digit][n - 1];
        }
        return totalCount;
    }
}
