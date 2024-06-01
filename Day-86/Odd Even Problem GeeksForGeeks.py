class Solution:
    def oddEven(self, s : str) -> str:
        x, y = 0, 0
        hashMap = {}
        for i in s:
            temp = ord(i) - ord('a') + 1
            if temp in hashMap:
                hashMap[temp] += 1
            else:
                hashMap[temp] = 1
        
        keys = list(hashMap.keys())
        for i in keys:
            if i%2 == 0 and hashMap[i]%2 == 0:
                x += 1
            elif i%2 == 1 and hashMap[i]%2 == 1:
                y += 1
                
        return "ODD" if (x+y)%2 == 1 else "EVEN"

