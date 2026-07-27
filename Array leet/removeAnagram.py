class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for word in words:
            if not result or sorted(word) != sorted(result[-1]):
                result.append(word)
        return result
