class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1 = set(nums)
        if len(s1) < 3:
            return max(s1)
        s1.remove(max(s1))
        s1.remove(max(s1))
        return max(s1)