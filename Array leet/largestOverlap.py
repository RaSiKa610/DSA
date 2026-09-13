import collections

class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)

        ones_img1 = []
        ones_img2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones_img1.append((i,j))
                if img2[i][j] == 1:
                    ones_img2.append((i,j))

        shift_counts = collections.defaultdict(int)

        for r1, c1 in ones_img1:
            for r2, c2 in ones_img2:
                shift_vec = (r2-r1, c2-c1)
                shift_counts[shift_vec] += 1

        return max(shift_counts.values()) if shift_counts else 0
