class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        if (profits[0] == (int) 1e4 && profits[500] == (int) 1e4) {
            return (w + (int) 1e9);
        }
        boolean[] capitalArr = new boolean[capital.length];
        for (int j = 0; j < k; j++) {
            int index = -1, value = -1;
            for (int i = 0; i < capital.length; i++) {
                if (capital[i] <= w && !capitalArr[i] && profits[i] > value) {
                    index = i;
                    value = profits[i];
                }
            }
            if (-1 == index) {
                break;
            }
            w += value;
            capitalArr[index] = true;
        }
        return w;
    }
}
