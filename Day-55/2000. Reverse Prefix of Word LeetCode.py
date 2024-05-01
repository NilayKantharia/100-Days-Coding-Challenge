class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        f = 0
        for i in range(len(word)):
            if word[i] == ch:
                f = 1
                break
        if not f:
            return word
        s = ""
        for j in range(i, -1, -1):
            s += word[j]
        for j in range(i + 1, len(word)):
            s += word[j]
        return s
        
