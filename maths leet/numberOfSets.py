import math
class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        N = n + k - 1
        K = 2 * k
        
        # Calculate N choose K: N! / (K! * (N - K)!)
        combinations = math.factorial(N) // (math.factorial(K) * math.factorial(N - K))
        
        return combinations % MOD
