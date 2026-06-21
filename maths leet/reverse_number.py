class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxi = 2**31

        res = 0
        num = abs(x)

        while num > 0:
            d = num % 10
            num //= 10

            if res > (maxi - d) // 10:
                return 0
            res = (res*10) + d
        return -res if x < 0 else res
