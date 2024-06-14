class Solution {
    static String armstrongNumber(int n){
        int res = 0;
        int rem = n;
        for(int i=0; i < 3; i++){
            res += Math.pow(rem%10, 3);
            rem /= 10;
        }
        return res == n? "Yes": "No";
    }
}
