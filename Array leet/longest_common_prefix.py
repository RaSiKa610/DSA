class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i, char in enumerate(zip(*strs)):
            if len(set(char)) > 1:
                return strs[0][:i]
        
        return min(strs, key=len)
