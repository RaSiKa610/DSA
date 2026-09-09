class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 999:
            return 0

        size = len(str(n))
        if 4 <= size <= 6:
            result = n - 999

        elif 7 <= size <= 9:
            result =  (n - 999999) * 2 + 999000

        elif 10 <= size <= 12:
            result =  (n - 999999999) * 3 + 999000000 * 2 + 999000

        elif 13 <= size <= 15:
            result =  (n - 999999999999) * 4 + 999000000000 * 3 + 999000000 * 2 + 999000
        else:
            result =  (n - 999999999999999) * 5 + 999000000000000 * 4 + 999000000000 * 3 + 999000000 * 2 + 999000

        return result
