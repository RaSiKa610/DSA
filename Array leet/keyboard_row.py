class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        c = []
        r1 = set('qwertyuiop')
        r2 = set('asdfghjkl')
        r3 = set('zxcvbnm')

        for word in words:
            s = set(word.lower())

            if s.issubset(r1) or s.issubset(r2) or s.issubset(r3):
                c.append(word)

        return c
                
        