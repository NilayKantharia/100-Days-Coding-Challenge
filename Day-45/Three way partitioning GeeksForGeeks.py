#User function template for Python

class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, array, a, b):
	    i = 0
	    idx = 0
	    while i < n and idx < n:
	        if array[idx] < a:
	            array.insert(0, array.pop(idx))
	            idx += 1
	        elif array[idx] > b:
	            array.append(array.pop(idx))
	        else:
	            idx += 1
	        i += 1
