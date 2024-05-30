class Solution {
    public int countTriplets(int[] arr) {
        int n = arr.length;
        int res = 0;
        for(int i=0; i<n-1; i++){
            int curr = arr[i];
            for(int j=i+1; j<n; j++){
                curr ^= arr[j];
                if(curr == 0){
                    res += j-i;
                }
            }
        }
        return res;
    }
}
