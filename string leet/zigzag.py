class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        res = [""] * numRows
        current = 0
        d = -1

        for i in s:
            res[current] += i

            if current == 0 or current == numRows -1:
                d *=-1

            current += d
        return "".join(res)
