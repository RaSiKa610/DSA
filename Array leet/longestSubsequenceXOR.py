class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Scenario 1: All elements are 0
        if all(x == 0 for x in nums):
            return 0
        
        # Calculate the XOR sum of the entire array
        total_xor = 0
        for num in nums:
            total_xor ^= num
            
        # Scenario 2: The total XOR is already non-zero
        if total_xor != 0:
            return len(nums)
        
        # Scenario 3: Total XOR is 0, but there are non-zero elements
        return len(nums) - 1
