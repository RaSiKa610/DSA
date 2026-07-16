from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        words = s1.split() + s2.split()

        counts = Counter(words)

        return [word for word in counts if counts[word] == 1]
