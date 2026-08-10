class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 9:
            return False
        i = 10
        flag = 1
        while i <= n:
            n = n - i
            i -= 1
            flag = 0 if flag == 1 else 1

        if flag == 1:
            return False
        else:
            return True
