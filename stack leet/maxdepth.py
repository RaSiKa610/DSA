class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 0

        max_len = 0
        stack = []
        for ch in s:
            if stack and ch == ')':
                stack.pop()
            elif ch == '(':
                stack.append(ch)
                max_len = max(max_len, len(stack))
            else:
                continue

        return max_len
