class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        arr = [(value, index) for index, value in enumerate(nums)]

        # Step 2: Sort by value
        arr.sort()

        n = len(nums)
        i = 0

        # Step 3: Process every group
        while i < n:

            j = i + 1

            # Find all values connected to this group
            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            # Step 4: Get original positions
            indices = [arr[k][1] for k in range(i, j)]

            # Put values into earliest positions
            indices.sort()

            for k in range(j - i):
                nums[indices[k]] = arr[i + k][0]

            i = j

        return nums
