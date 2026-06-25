class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k = k - 1
        l = [str(i) for i in range(1, n+1)]

        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i-1] * i

        res = []

        for i in range(n-1, -1,-1):
            index = k // fact[i]
            res.append(l.pop(index)) 
            k %= fact[i]

        return "".join(res)
