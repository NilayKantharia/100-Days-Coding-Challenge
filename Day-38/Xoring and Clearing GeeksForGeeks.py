class Solution:
    def printArr(self, n, arr):
        for i in range(n-1):
            print(arr[i],end=' ')
        print(arr[n-1])
        

    def setToZero(self, n, arr):
        for i in range(n):
            arr[i] = 0
        

    def xor1ToN(self, n, arr):
        for i in range(n):
            arr[i] = arr[i] ^ i
        
