class Solution:
    def helper(self, arr, target):
        count = 0
        i = 0
        n = len(arr)
        num = arr[0]
        deno = arr[n - 1]
        for j in range(1,n):
            while arr[i] <= arr[j]*target:
                i += 1
            count += i
            if i > 0 and arr[i - 1] * deno > arr[j] * num:
                num = arr[i - 1]
                deno = arr[j]
        return [count, num, deno]

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        low = arr[0]/float(arr[n - 1])
        high = 1
        while low < high:
            mid = (low + high)/2
            count = self.helper(arr, mid)
            print(count,low,mid,high)
            if k < count[0]:
                high = mid
            elif k > count[0]:
                low = mid
            else:
                return [count[1], count[2]]

