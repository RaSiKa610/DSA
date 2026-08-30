class Solution:
    def minimumDeletions(self, nums):

        n = len(nums)

        # Find indices of minimum and maximum
        minIndex = 0
        maxIndex = 0

        for i in range(n):
            if nums[i] < nums[minIndex]:
                minIndex = i

            if nums[i] > nums[maxIndex]:
                maxIndex = i

        # Put the smaller index first
        left = min(minIndex, maxIndex)
        right = max(minIndex, maxIndex)

        # Three possible strategies
        front = right + 1
        back = n - left
        mixed = (left + 1) + (n - right)

        return min(front, back, mixed)
