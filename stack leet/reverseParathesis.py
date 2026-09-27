class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if ch == ')':
                word = []
                while  stack and stack[-1] != '(':
                    word.append(stack.pop())
                if stack:
                    stack.pop() 
                stack.extend(word)
            else:
                stack.append(ch)

        return "".join(stack)
