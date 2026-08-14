class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
        # Add the current character to the frequency map
            counts[s[right]] = counts.get(s[right], 0) + 1

            # Shrink the window from the left if any character exceeds 2 occurrences
            while counts[s[right]] > 2:
                counts[s[left]] -= 1
                left += 1

            # Update the maximum valid substring length
            max_len = max(max_len, right - left + 1)

        return max_len
