class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        seen = set()
        dup = -1

        for i in nums:
            if i in seen:
                dup = i
            seen.add(i)

        total = n * (n+1) // 2
        miss = total - (sum(nums) - dup)
        return [dup, miss]
