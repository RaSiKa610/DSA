class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        n = len(nums)

        prefix_sum_left = [0] * (n+1)
        prefix_sum_right = [0] * (n+1)

        for i in range(1, n+1):
            prefix_sum_left[i] = prefix_sum_left[i - 1] + nums[i - 1]

        for i in range(n -1, -1, -1):
            prefix_sum_right[i] = prefix_sum_right[i+1] + nums[i]

        for i in range(n):
            if prefix_sum_right[i+1] == prefix_sum_left[i]:
                return i

        return -1
