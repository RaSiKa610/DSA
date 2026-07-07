class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        n += 1
        c = [1] * n
        for i in range(2, n):
            c[i] = c[i-1] + c[i - 2]

        return c[-1]
