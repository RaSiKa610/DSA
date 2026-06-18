class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def addzero(x, m):
            return x[::-1] + ("0" * m)
        if len(a) > len(b):
            n = len(a)
            b = addzero(b, len(a)-len(b))
            a = a[::-1]
        else:
            n = len(b)
            a = addzero(a, len(b)-len(a))
            b = b[::-1]
        
        carry = 0 
        res = ""
        
        for i in range(n):
            bit_a = int(a[i])
            bit_b = int(b[i])

            total = bit_a + bit_b + carry

            res += str(total % 2)
            carry = total // 2

        if carry:
            res += "1"
        return res[::-1]
