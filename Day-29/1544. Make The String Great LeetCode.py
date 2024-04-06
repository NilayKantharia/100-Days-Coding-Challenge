class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if(stack and 
                stack[-1].lower() == s[i].lower() and 
                ((stack[-1].islower() and s[i].isupper()) or (stack[-1].isupper() and s[i].islower()))):
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
