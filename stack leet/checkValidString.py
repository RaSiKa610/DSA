class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        stack_2 = []
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == '*':
                stack_2.append(i)
            elif ch == ')':
                if stack:
                    stack.pop()
                elif stack_2:
                    stack_2.pop()
                else:
                    return False

        while stack and stack_2:
            if stack[-1] < stack_2[-1]:
                stack.pop()
                stack_2.pop()
            else:
                return False

        return not stack
