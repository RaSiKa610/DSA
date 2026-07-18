class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = min(nums)
        a = max(nums)
        r = a % b
        while r != 0:
            a = b
            b = r
            r = a % b

        return b
