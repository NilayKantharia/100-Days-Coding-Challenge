class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        # hashSet = set(arr)
        # for i in range(n):
        #     if abs(x + arr[i]) in hashSet:
        #         return 1
        # return -1
        
        
        if x == 0: 
            if len(arr) == len(set(arr)):
                return -1
            else:
                return 1
            
        arr.sort()
        l = 0
        r = 1
        while r < n:
            d = abs(arr[r] - arr[l])
            if d == x:
                return 1
            elif d < x:
                r += 1
            elif d > x:
                l += 1
        return -1
