class Solution:    
    def merge(self, arr, low, mid, high):
        i = low
        j = mid + 1
        inv = 0
        temp = []

        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                inv += mid - i + 1
                j += 1
        
        while i <= mid:
            temp.append(arr[i])
            i += 1
        
        while j <= high:
            temp.append(arr[j])
            j += 1
        
        for i in range(low, high + 1):
            arr[i] = temp[i - low]
        
        return inv
    
    def mergeSort(self, arr, low, high):
        if low >= high : return 0
        count = 0
        mid = low + (high - low) // 2
        count += self.mergeSort(arr, low, mid)
        count += self.mergeSort(arr, mid + 1, high)
        count += self.merge(arr, low, mid, high)
        return count
            
    
    def countPairs(self,arr, n): 
        for i in range(n):
            arr[i] = arr[i] * i
        return self.mergeSort(arr, 0, n - 1)
