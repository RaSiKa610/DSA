class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        left, r = 0, x
        ans = 0

        while left <= r:
            mid = left + (r-left) // 2
            num = mid * mid
            if num == x:
                return mid
            elif num < x:
                ans = mid 
                left = mid + 1
            else:
                r = mid - 1
        return ans
