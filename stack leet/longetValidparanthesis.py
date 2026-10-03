class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        stack = [-1]
        max_len = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            if ch == ')':
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    curr_len = i - stack[-1]
                    max_len = max(max_len, curr_len)

        return max_len
