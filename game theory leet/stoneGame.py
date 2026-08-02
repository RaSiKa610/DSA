class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        memo  = {}

        def solve(i,j):
            if i > j:
                return 0
            if i == j:
                return piles[i]

            if (i, j) in memo:
                return memo[(i,j)]

            take_i = piles[i] + min(solve(i+2, j), solve(i+1, j-1))
            take_j = piles[j] + min(solve(i+1, j-1), solve(i, j-2))

            memo[(i, j)] = max(take_i, take_j)
            return memo[(i, j)]

        p1 = solve(0, n-1)
        return p1 >= sum(piles) - p1
