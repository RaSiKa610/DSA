from collections import Counter

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a, b):
            r = a % b
            while r!=0:
                a = b
                b = r
                r = a % b

            return b

        counts = Counter(deck).values()

        current_gcd = 0
        for count in counts:
            current_gcd = gcd(current_gcd, count)

        return current_gcd >= 2
