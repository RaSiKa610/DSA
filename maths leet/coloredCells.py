class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        ans = 1
        for i in range(1, n):
            ans += i * 4

        return ans
