class Solution(object):
    def smallestSubsequence(self, s):
        """ 
        :type s: str
        :rtype: str
        """
        dict = {char: i for i, char in enumerate(s)}
        stack = []
        seen = set()

        for i , char in enumerate(s):
            if char in seen:
                continue

            while stack and stack[-1] > char and dict[stack[-1]] > i:
                rem = stack.pop()
                seen.remove(rem)
            
            stack.append(char)
            seen.add(char)

        return "".join(stack)
