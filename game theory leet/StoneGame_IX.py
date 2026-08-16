class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        # If either remainder 1 or 2 is missing
        if count[1] == 0 or count[2] == 0:
            return max(count[1], count[2]) > 2 and count[0] % 2 == 1

        # Both remainder 1 and 2 exist
        return abs(count[1] - count[2]) > 2 or count[0] % 2 == 0
