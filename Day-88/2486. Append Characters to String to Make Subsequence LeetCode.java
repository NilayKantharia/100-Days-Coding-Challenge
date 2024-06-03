class Solution {
    public int appendCharacters(String s, String t) {
        int i = -1, j = 0, n1 = s.length(), n2 = t.length();
        while(++i < n1 && j < n2){
            if(s.charAt(i) == t.charAt(j)){
                j++;
            }
        }
        return n2 - j;
    }
}
