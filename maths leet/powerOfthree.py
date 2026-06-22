class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        i = 3

        while i <= n:
            if i == n:
                break
            i *= 3

        if n == 1 or i == n:
            return True
        else:
            return False
