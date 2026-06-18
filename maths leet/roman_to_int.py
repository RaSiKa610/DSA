class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        r = 0
        m = 0

        for i in reversed(s):
            val = dic[i]
            if val < m:
                r -= val
            else:
                r += val
                m = val
        return r
