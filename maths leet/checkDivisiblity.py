class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dupli = n
        add = 0
        product = 1
        while n != 0:
            s = n % 10
            add += s
            product *= s
            n = n // 10

        if dupli % (product + add) == 0:
            return True
        
        return False
