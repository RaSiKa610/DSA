class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = 0
        maxi = 0
        for i in nums:
            if i == 1:
                flag += 1
            else:
                maxi = max(maxi, flag)
                flag = 0

            
        return max(maxi, flag)
                    