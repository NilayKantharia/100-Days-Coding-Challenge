class Solution:

    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        i = 0
        if k < arr[0]:
            return arr[0]
        while i < n - 1:
            if k >= arr[i] and k <= arr[i + 1]:
                break
            i += 1 
        if i < n - 1:
            return arr[i] if k - arr[i] < arr[i + 1] - k else arr[i + 1]
        else:
            return arr[n - 1]
