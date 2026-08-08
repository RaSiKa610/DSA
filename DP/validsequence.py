class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)

        # last[j] stores the largest starting index in word1 from which 
        # word2[j:] can be formed as a exact subsequence without changes.
        last = [-1] * (m + 1)
        last[m] = n

        ptr = n - 1
        for j in range(m - 1, -1, -1):
            while ptr >= 0 and word1[ptr] != word2[j]:
                ptr -= 1
            last[j] = ptr
            if ptr >= 0:
                ptr -= 1

        ans = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break

            # Case 1: Exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            # Case 2: Mismatch, try using our single replacement if not used yet
            elif not changed and last[j + 1] > i:
                ans.append(i)
                j += 1
                changed = True

        return ans if len(ans) == m else []
