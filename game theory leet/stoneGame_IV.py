class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        memo = {}
        def solve(x):
            if x == 0:
                return False

            if x in memo:
                return memo[x]

            i = 1
            while i*i <= x:
                if not solve(x - i*i):
                    memo[x] = True
                    return True
                i += 1
            memo[x] = False
            return memo[x]

        return solve(n)   
