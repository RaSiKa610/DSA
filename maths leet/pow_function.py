class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 /x
            n = -n
        return self.fastPow(x,n)

    def fastPow(self, x, n):
        if n == 0:
            return 1.0
        h = self.fastPow(x, n//2)

        if n % 2 == 0:
            return h * h
        else:
            return h * h * x
