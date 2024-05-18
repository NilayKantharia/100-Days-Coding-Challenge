class Solution:
	def findPeakElement(self, a):
		n = len(a)
		i = n // 2
        mx = 0
		if n == 1 or n == 2:
		    return a[-1]
		if a[i] > a[i - 1] and a[i] > a[i + 1]:
		    return a[i] if a[i] > a[n - 1] else a[n - 1]
        elif a[i + 1] > a[i]:
            mx = 0
            while i < n:
                mx = max(mx, a[i])
                i += 1
        else:
            while i > 0:
                mx = max(mx, a[i])
                i -= 1
        return mx
