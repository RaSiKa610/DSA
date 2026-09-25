import heapq
from collections import Counter

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = []

        for i in range(n - k + 1):
            window = nums[i:i+k]
            counts = Counter(window)
            min_heap = []

            for val, freq in counts.items():
                heapq.heappush(min_heap, (freq, val))

                if len(min_heap) > x:
                    heapq.heappop(min_heap)

            current_sum = 0
            for freq, val in min_heap:
                current_sum += freq * val

            ans.append(current_sum)
        return ans
