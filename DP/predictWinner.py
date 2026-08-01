class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = {}

        def get_max_diff(i, j):
            if i == j:
                return nums[i]
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Player chooses either the leftmost element (i) or rightmost element (j)
            pick_left = nums[i] - get_max_diff(i + 1, j)
            pick_right = nums[j] - get_max_diff(i, j - 1)
            
            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]

        return get_max_diff(0, len(nums) - 1) >= 0
