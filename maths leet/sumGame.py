class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        
        # Track sums (s1, s2) and question mark counts (q1, q2) for both halves
        s1, s2 = 0, 0
        q1, q2 = 0, 0
        
        # Process the first half
        for i in range(n // 2):
            if num[i] == '?':
                q1 += 1
            else:
                s1 += int(num[i])
                
        # Process the second half
        for i in range(n // 2, n):
            if num[i] == '?':
                q2 += 1
            else:
                s2 += int(num[i])

        if (q1 + q2) % 2 != 0:
            return True

        if s1 - s2 == (q2 - q1) * 9 // 2:
            return False  # Bob wins
            
        return True
