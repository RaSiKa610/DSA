import heapq
from collections import Counter

class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counts = Counter(arr)

        max_heap = [-x for x in counts.values()]
        heapq.heapify(max_heap)
        
        target_size = len(arr) // 2
        rem_ele = 0
        set_size = 0

        while rem_ele < target_size:
            rem_ele += -heapq.heappop(max_heap)
            set_size += 1

        return set_size
