class Solution {
    public static int maxOccured(int n, int l[], int r[], int maxx) {
        int arr[] = new int[maxx+2];
        for(int i=0; i<n; i++){
            arr[l[i]]++;
            arr[r[i]+1]--;
        }
        int sum = 0, ans=0;
        for(int i=0; i<maxx; i++){
            arr[i] += sum;
            sum = arr[i];
            if(arr[i]>arr[ans]){
                ans = i;
            }
        }
        return ans;
    }
}
