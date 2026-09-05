class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
            
        # Step 1: Precompute the minimums from the right (suffix minimums)
        suff_min = [0] * n
        suff_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])
            
        # Step 2: Iterate from the left, tracking the prefix maximum
        pref_max = nums[0]
        for i in range(n):
            pref_max = max(pref_max, nums[i])
            
            # Step 3: Check if the instability score is <= k
            if pref_max - suff_min[i] <= k:
                return i
                
        return -1
