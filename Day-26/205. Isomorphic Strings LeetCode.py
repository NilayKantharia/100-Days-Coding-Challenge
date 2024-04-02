class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashMap = {}
        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = t[i]
            else:
                if hashMap[s[i]] != t[i]:
                    return False
        return len(set(hashMap.values())) == len(hashMap)
