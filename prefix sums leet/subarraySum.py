class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        res = 0
        prefix_counts = {0: 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix_counts:
                res += prefix_counts[prefix_sum - k]

            prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1

        return res
