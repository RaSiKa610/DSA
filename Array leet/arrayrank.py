class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ranks = {num: i + 1 for i, num in enumerate(sorted(set(arr)))}
        return [ranks[num] for num in arr]
