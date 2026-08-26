class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        best = ""
        l = 0
        ones = 0

        for r in range(len(s)):
            if s[r] == "1":
                ones += 1

            while ones == k:
                current = s[l:r+1]
                if best == "" or len(current) < len(best) or (len(current) == len(best) and current < best):
                    best = current

                if s[l] == "1":
                    ones -= 1
                l += 1

        return best
