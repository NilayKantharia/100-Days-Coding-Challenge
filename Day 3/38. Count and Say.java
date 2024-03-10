class Solution {
    public String countAndSay(int n) {
        String s = "1";
        for(int i=1;i<n;i++){
            s=fun1(s);
        }
        return s;
    }
    public String fun1(String s){
        StringBuilder sb = new StringBuilder();
        char p = s.charAt(0);
        int count = 1;
        int len=s.length();
        for(int i=1;i<len;i++){
            if (s.charAt(i)==p){
                count++;
            }
            else{
                sb.append(count);
                sb.append(p);
                p=s.charAt(i);
                count=1;
            }
        }
        sb.append(count);
        sb.append(p);
        return sb.toString();
    }
}
