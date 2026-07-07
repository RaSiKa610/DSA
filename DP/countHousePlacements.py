class Solution(object):
    def countHousePlacements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        a, b = 1, 2 
        for _ in range(2, n+1):
            a, b = b, (a + b) % MOD
        return (b * b) % MOD
