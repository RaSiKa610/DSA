class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        
        # dp[j] will store the number of ways to form t[:j]
        dp = [0] * (n + 1)
        
        # Base case: 1 way to form an empty string t
        dp[0] = 1
        
        for i in range(1, m + 1):
            # Traverse backwards to avoid overwriting values needed for the current step
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] = dp[j] + dp[j - 1]
                    
        return dp[n]
