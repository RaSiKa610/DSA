class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        mx = float('-inf')
        for val in nums:
            if val == 1:
                count += 1
            else:
                mx = max(mx,count)
                count = 0

        return max(mx, count)
