class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = [int(i) for i in str(n)]

        s.sort()
        return s[-1] * s[-2]
