class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        word = {'b':1, 'a':1, 'l':2, 'o':2, 'n':1}
        f = Counter(text)
        r = []

        for i in word:
            found = word[i]
            available = f[i]
            p = available // found
            r.append(p)

        return min(r)
