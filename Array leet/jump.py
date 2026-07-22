class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We don't need to process the last element (n - 1)
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            
            # When we reach the boundary of the current jump range,
            # we must make another jump.
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Early exit if we can already reach or pass the end
                if current_end >= n - 1:
                    break
                    
        return jumps
