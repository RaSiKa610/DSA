class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = list(str(n))
        n = len(digits)
        flag = n

        for i in range(n-1, 0, -1):
            if digits[i-1] > digits[i]:
                digits[i-1] = str(int(digits[i-1]) - 1)
                flag = i

        for i in range(flag, n):
            digits[i] = '9'

        return int("".join(digits))
