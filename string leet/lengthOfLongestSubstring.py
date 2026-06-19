class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        v = set()
        l = 0
        maxi = 0

        for r in range(len(s)):
            while s[r] in v:
                v.remove(s[l])
                l += 1
            v.add(s[r])
            maxi = max(maxi, r-l+1)

        return maxi
