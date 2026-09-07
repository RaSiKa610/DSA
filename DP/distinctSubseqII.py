class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        end = [0] * 26

        for c in s:
            indx = ord(c) - ord('a')
            total = sum(end) % MOD
            end[indx] = (total + 1) % MOD

        return sum(end) % MOD
