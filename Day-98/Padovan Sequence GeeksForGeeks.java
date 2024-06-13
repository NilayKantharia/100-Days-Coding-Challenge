class Solution
{
  public int padovanSequence(int n)
    {
        int mod = 1000000007;
        if(n <= 2)
            return 1;
        int p[] = new int[n+1];
        p[0] = 1; p[1] = 1; p[2] = 1;
        for(int i = 3; i <= n; i++){
            p[i] = (p[i - 2] + p[i - 3]) % mod;
        }
        return p[n];
    }
    
}
