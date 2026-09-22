import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            f = heapq.heappop(stones)
            s = heapq.heappop(stones)
            if f != s:
                heapq.heappush(stones, f-s)

        return -stones[0] if stones else 0
