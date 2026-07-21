class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        initial_ones = s.count('1')

        t = '1' + s + '1'

        seg = []
        i = 0
        n = len(t)

        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            seg.append((t[i], j - i))
            i = j
        
        max_delta = 0
        for k in range(1, len(seg) - 1):
            char, _ = seg[k]
            if char == '1':
                if seg[k-1][0] == '0' and seg[k+1][0] == '0':
                    delta = seg[k-1][1] + seg[k+1][1]
                    max_delta = max(max_delta, delta)
        return initial_ones + max_delta
