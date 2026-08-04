class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mini = min(nums)
        maxi = max(nums)
        result = []

        for i in range(mini + 1, maxi):
            if i not in nums:
                result.append(i)

        return result
