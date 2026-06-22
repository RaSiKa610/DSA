class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        min_d = float('inf')

        for r in range(k-1, len(nums)):
            l = r - k + 1
            min_d = min(min_d, nums[r] - nums[l])

        return min_d
