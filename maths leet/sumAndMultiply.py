class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        f = ''.join([i for i in s if i != '0'])
        if not f:
            return 0

        sum_int = sum(int(i) for i in f)

        return int(f) * sum_int
