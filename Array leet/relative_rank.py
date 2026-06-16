class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        res = [""] * len(score)
        sort = sorted(enumerate(score), key=lambda x: x[1], reverse = True)

        for rank, (ori_index, s) in enumerate(sort):
            if rank == 0:
                res[ori_index] = "Gold Medal"
            elif rank == 1:
                res[ori_index] = "Silver Medal"
            elif rank == 2:
                res[ori_index] = "Bronze Medal"
            else:
                res[ori_index] = str(rank + 1)

        return res
            