import heapq

class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        def soldier_count(row):
            l, r = 0, len(row) - 1
            while l <= r:
                mid = l + (r-l)//2
                if row[mid] == 1:
                    l = mid + 1
                else:
                    r = mid - 1

            return l

        max_heap = []

        for i, row in enumerate(mat):
            soldiers = soldier_count(row)
            heapq.heappush(max_heap, (-soldiers, -i))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        res = []
        while max_heap:
            res.append(-heapq.heappop(max_heap)[1])

        return res[::-1]
