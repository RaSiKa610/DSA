class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums) - 1
            while l < r:
                current = nums[i] + nums[l] + nums[r]
                if current == target:
                    return current
                if abs(target - current) < abs(target - closest_sum):
                    closest_sum = current

                if current < target:
                    l += 1
                else:
                    r -= 1
        return closest_sum
