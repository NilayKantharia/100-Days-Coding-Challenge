class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        res = []
        i = 0
        j = 0
        hashSet = set()
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                if arr1[i] not in hashSet:
                    res.append(arr1[i])
                    hashSet.add(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                if arr2[j] not in hashSet:
                    res.append(arr2[j])
                    hashSet.add(arr2[j])
                j += 1
            elif arr1[i] == arr2[j]:
                if arr1[i] not in hashSet:
                    hashSet.add(arr1[i])
                    res.append(arr1[i])
                i += 1
                j += 1
                
        while i < n:
            if arr1[i] not in hashSet:
                res.append(arr1[i])
                hashSet.add(arr1[i])
            i += 1
        while j < m:
            if arr2[j] not in hashSet:
                res.append(arr2[j])
                hashSet.add(arr2[j])
            j += 1
        return res
