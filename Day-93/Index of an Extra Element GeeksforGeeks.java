class Solution {
    public int findExtra(int n, int arr1[], int arr2[]) {
        int i = 0, j = 0;
        while(i<n && j<n-1){
            if(arr1[i] != arr2[j]) return i;
            else {
                i++; j++;
            }
        }
        return n-1;
    }
}
