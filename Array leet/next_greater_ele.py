class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        stack = []
        for i in reversed(nums2):
            while stack and stack[-1] <= i:
                stack.pop()

            d[i] = stack[-1] if stack else -1
            stack.append(i)

        return [d[i] for i in nums1]
