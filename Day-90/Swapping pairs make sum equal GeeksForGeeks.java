class Solution {
    long findSwapValues(long a[], int n, long b[], int m) {
        int sumA = 0, sumB = 0;
        for(int i=0; i<n; i++) sumA += a[i];
        for(int i=0; i<m; i++) sumB += b[i];
        if((sumA-sumB)%2 != 0) return -1;
        int res = (sumA-sumB)/2;
        Arrays.sort(a);
        Arrays.sort(b);
        int i = 0, j = 0;
        while (i < n && j < m){
            long diff = a[i]-b[j];
            if(diff == res) return 1;
            else if(diff > res) j++;
            else i++;
        }
        return -1;
    }
}
