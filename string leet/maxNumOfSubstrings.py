class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i

        def helper(start):
            end = last[s[start]]
            i = start

            while i <= end:
                if first[s[i]] < start:
                    return -1

                end = max(end, last[s[i]])
                i += 1

            return end

        valid_windows = []
        for char in set(s):
            start = first[char]
            end = helper(start)

            if end != -1:
                valid_windows.append((start, end))

        valid_windows.sort(key=lambda x: x[1])

        result = []
        last_added_end = -1
        for start, end in valid_windows:
            if start > last_added_end:
                result.append(s[start:end + 1])
                last_added_end = end

        return result
