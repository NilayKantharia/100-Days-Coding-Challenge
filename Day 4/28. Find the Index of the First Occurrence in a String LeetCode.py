class Solution {
    public int strStr(String haystack, String needle) {
        int i=0,j=0;
        int l1=haystack.length();
        int l2=needle.length();
        while (i<l1){
            if(haystack.charAt(i)==needle.charAt(j)){
                while(i<l1 && j<l2 && haystack.charAt(i)==needle.charAt(j)){
                    i++;
                    j++;
                    if (j==l2)
                        return i-j;
                }
                i=i-j;
            }
            i++;
            j=0;
        }
        return -1;
    }
}
