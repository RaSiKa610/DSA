class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        running_sum = 0

        diff_arr = {0:-1}

        for i, num in enumerate(nums):
            if num == 1:
                running_sum += 1
            else:
                running_sum -= 1

            if running_sum in diff_arr:
                sub_idx = diff_arr[running_sum]
                max_len = max(max_len, i - sub_idx)

            else:
                diff_arr[running_sum] = i

        return max_len
