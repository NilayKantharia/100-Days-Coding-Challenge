class Solution:
    def binaryNextNumber(self, s):
        res = ""
        carry = 1
        for i in reversed(s):
            if i == '1':
                if carry:
                    res += '0'
                else:
                    res += '1'
            elif carry:
                res += '1'
                carry -= 1
            else:
                res += '0'
        if carry:
            res += '1'
        res = res[::-1]
        while res and res[0] == '0':
            res = res[1:]
        return ''.join(res)
