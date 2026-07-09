class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in range(len(nums)):
            l = sum(nums[:i]) 
            r = sum(nums[i+1:])
            if l == r:
                return i

        return -1
