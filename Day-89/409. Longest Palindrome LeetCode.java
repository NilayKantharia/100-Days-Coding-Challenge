class Solution {
    public int longestPalindrome(String s) {
        int n = s.length();
        int odds = 0;
        Map<Character, Integer> hashMap = new HashMap<>();
        for(int i=0; i<n; i++){
            char curr = s.charAt(i);
            hashMap.put(curr, hashMap.getOrDefault(curr, 0) + 1);
            
            if(hashMap.get(curr) % 2 == 1){
                odds++;
            }else{
                odds--;
            }
        }
        return odds > 0 ? n - odds + 1 : n; 
    }
}
