class Solution(object):
    def maxScore(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        memo = {}
        def choose(i, p):
            if i == len(nums):
                return 0

            if (i, p) in memo:
                return memo[(i, p)]

            pick = 0
            if (nums[i] % 2) == p:
                pick = nums[i] + choose(i+1, p)
            else:
                pick = nums[i] - x + choose(i+1, 0 if p==1 else 1)

            notpick = choose(i+1, p)
            memo[(i, p)] = max(pick, notpick)
            return memo[(i, p)]

        return nums[0] + choose(1, nums[0] % 2)
