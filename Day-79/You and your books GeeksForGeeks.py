class Solution:
    #Your task is to complete this function
    #Function should return an integer
    #a - list/array containing height of stack's respectively
    def max_Books(self, n, k, arr):
        maxBooks = 0
        currBooks = 0
        for r in range(n):
            if arr[r] <= k:
                currBooks += arr[r]
                maxBooks = max(maxBooks, currBooks)
            else:
                currBooks = 0
        return maxBooks
