class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        u = sorted(set(nums))
        nums[:] = u
        return len(u)