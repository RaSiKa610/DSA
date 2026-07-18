class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = n - 1
        count = 2
        while i > 1:
            if n % i == 0:
                count += 1
            i -= 1
            if count > 3:
                return False

        return count == 3 
