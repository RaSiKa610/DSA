class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        memo = {}

        def solveAlice(person, i, m):
            if i >= n:
                return 0

            if (person, i, m) in memo:
                return memo[(person, i, m)]

            stones = 0
            # Alice wants to maximize her score
            if person == 1:
                result = -1
                # Range goes up to min(n - i, 2 * m) inclusive
                for x in range(1, min(n - i, 2 * m) + 1):
                    stones += piles[i + x - 1]
                    result = max(result, stones + solveAlice(0, i + x, max(m, x)))
            # Bob wants to minimize Alice's score
            else:
                result = float('inf')
                for x in range(1, min(n - i, 2 * m) + 1):
                    # Bob gains stones, but Alice gets 0 from Bob's turn
                    result = min(result, solveAlice(1, i + x, max(m, x)))

            memo[(person, i, m)] = result
            return result

        return solveAlice(1, 0, 1)
