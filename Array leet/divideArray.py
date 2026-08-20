from collections import Counter

class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = Counter(nums)
        for num, freq in count.items():
            if freq % 2 == 1:
                return False

        return True
