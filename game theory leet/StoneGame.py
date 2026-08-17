class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        # dp[i][j] = maximum score for subarray i...j
        dp = [[0] * n for _ in range(n)]

        # mx[i][j] stores the maximum value needed
        # for the optimized transition.
        mx = [[0] * n for _ in range(n)]

        for i in range(n):
            mx[i][i] = stoneValue[i]

        for j in range(1, n):

            # mid separates the left and right parts
            mid = j

            left_sum = stoneValue[j]
            right_sum = 0

            for i in range(j - 1, -1, -1):

                left_sum += stoneValue[i]

                # Move mid while the right part can still
                # be <= left part.
                while mid > i and \
                        (right_sum + stoneValue[mid]) * 2 <= left_sum:

                    right_sum += stoneValue[mid]
                    mid -= 1

                # Equal sums
                if right_sum * 2 == left_sum:
                    dp[i][j] = mx[i][mid]

                # Left side is smaller
                if mid != i:
                    dp[i][j] = max(
                        dp[i][j],
                        mx[i][mid - 1]
                    )

                # Right side is smaller
                if mid != j:
                    dp[i][j] = max(
                        dp[i][j],
                        mx[j][mid + 1]
                    )

                # Update auxiliary maximum
                mx[i][j] = max(
                    mx[i][j - 1],
                    dp[i][j] + left_sum
                )

                # Store the same information in reverse direction
                mx[j][i] = max(
                    mx[j][i + 1],
                    dp[i][j] + left_sum
                )

        return dp[0][n - 1]
