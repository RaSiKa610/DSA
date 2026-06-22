class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = set()
        while n != 1 and n not in l:
            l.add(n)
            n = sum(int(i)**2 for i in str(n))

            
        if n == 1:
            return True
        else:
            return False
