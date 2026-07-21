class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = [0] * 102
        for num in nums:
            count[num+1] += 1
        for i in range(1, len(count)):
            count[i] += count[i-1]

        return [count[num] for num in nums]
