class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if pow(num, 0.5) == int(pow(num, 0.5)):
            return True
        else:
            return False
