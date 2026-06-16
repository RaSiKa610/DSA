class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        result = {}
        for i, num in enumerate(nums):
            if num in result and i - result[num] <= k:
                return True
            result[num] = i

        return False
