class Solution:
    def swapNibbles (self, n):
        a = n&240
        a >>= 4
        b = n&15
        b <<= 4
        return a|b
