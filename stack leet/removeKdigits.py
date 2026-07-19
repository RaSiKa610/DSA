class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return "0"
        stack = []

        for curr in num:
            while stack and stack[-1] > curr and k > 0:
                stack.pop()
                k -= 1
            stack.append(curr)

        stack = stack[:-k] if k > 0 else stack

        result = "".join(stack).lstrip('0')
        return result if result else "0"
