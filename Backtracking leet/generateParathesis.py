class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []


        def backtrack(curr, opened, close):
            if len(curr) == 2 * n:
                res.append(curr)
                return

            if opened < n:
                backtrack(curr + "(", opened + 1, close)

            if close < opened:
                backtrack(curr + ")", opened, close + 1)

        backtrack("", 0, 0)
        return res
