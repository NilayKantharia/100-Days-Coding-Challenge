class Solution:
    
    def twoRepeated(self, arr , n):
        res = []
        for i in range(n+2):
            idx = abs(arr[i])
            if arr[idx] > 0:
                arr[idx] *= -1
            else:
                res.append(idx)
        return res

