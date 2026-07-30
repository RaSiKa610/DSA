class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        flag = 1
        result = 0
        n = len(word)

        if n < 8:
            return n

        for _ in range(n//8):
            result = result + (flag * 8)
            flag += 1

        r = n % 8

        if r == 0:
            return result
        else:
            return (result + r * flag)
