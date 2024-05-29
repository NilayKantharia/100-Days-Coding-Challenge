class Solution:
    def findWinner(self, n : int, x : int, y : int) -> int:
        arr = [0] * (n + 2)
        arr[1] = 1
        for i in range(2, n+1):
            j = i - 1
            if j >= 0 and arr[j] == 0:
                arr[i] = 1
            
            j = i - x
            if j >= 0 and arr[j] == 0:
                arr[i] = 1
            
            j = i - y
            if j >= 0 and arr[j] == 0:
                arr[i] = 1
            
        return arr[n]
