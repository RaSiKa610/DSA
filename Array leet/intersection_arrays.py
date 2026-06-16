class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = sorted(set(nums1))
        s2 = sorted(set(nums2))
        result = []
        i = 0
        j = 0

        while i < len(s1) and j < len(s2):
            if s1[i] < s2[j]:
                i += 1
            elif s1[i] > s2[i]:
                j += 1
            else:
                result.append(s1[i])
                i += 1
                j += 1

        return result

            

        
        