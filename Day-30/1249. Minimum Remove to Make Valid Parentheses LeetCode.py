class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        res = s
        remove = 0
        for i in range(len(s)):
            if s[i] == '(':
                st.append(s[i])
            elif st and s[i] == ')' and st[-1] == '(':
                st.pop()
            elif s[i] in ('(',')'):
                remove += 1
                res = res[:i] + "@" + res[i+1:]

        n = len(res)            
        for i in range(n-1,-1,-1):
            if st and res[i] == st[-1]:
                res = res[:i] + '@' + res[i+1:]
                st.pop()
        return res.replace('@','')
