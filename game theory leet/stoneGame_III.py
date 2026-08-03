class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        memo = [-1] * (n+1)

        def solve(i):
            if i >= n:
                return 0

            if memo[i] != -1:
                return memo[i]

            result = stoneValue[i] - solve(i+1)
            if i+1 < n:
                result = max(result, stoneValue[i] + stoneValue[i+1] - solve(i+2))

            if i+2 < n:
                result = max(result, stoneValue[i] + stoneValue[i+1] +stoneValue[i+2]  - solve(i+3))
            memo[i] = result
            return memo[i]

        diff = solve(0)
        if diff < 0:
            return "Bob"
        elif diff > 0:
            return "Alice"
        return "Tie"
