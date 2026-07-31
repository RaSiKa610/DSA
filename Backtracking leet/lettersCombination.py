class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []
        def dfs(index, curr):

            if index == len(digits):
                ans.append(curr)
                return

            letters = phone[digits[index]]

            for ch in letters:
                dfs(index + 1, curr + ch)

        dfs(0, "")
        return ans
