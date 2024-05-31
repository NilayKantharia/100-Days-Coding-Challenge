class Solution {
    public int[] singleNumber(int[] nums) {
        int n = nums.length;
        int xor = 0;
        for(int i=0; i<n; i++){
            xor ^= nums[i];
        }
        int diff=1;
        while((diff&xor) == 0){
            diff <<= 1;
        }
        int res[] = new int[2];
        for(int i=0; i<n; i++){
            if((nums[i]&diff) == 0){
                res[0] ^= nums[i];
            }
            else{
                res[1] ^= nums[i];
            }
        }
        return res;
    }
}
