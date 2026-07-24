class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vals = list(set(nums))
        MAXX = 2048  # Maximum XOR value (nums[i] <= 1500)

        pair = [False] * MAXX
        trip = [False] * MAXX

        # All possible XORs of two values
        for x in vals:
            for y in vals:
                pair[x ^ y] = True

        # XOR each pair result with every value
        for p in range(MAXX):
            if pair[p]:
                for x in vals:
                    trip[p ^ x] = True

        return sum(trip)
