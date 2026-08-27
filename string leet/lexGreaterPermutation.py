class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        freq = [0] * 26
        
        # Step 1: Count character frequencies in s
        for char in s:
            freq[ord(char) - ord('a')] += 1
            
        # Step 2: Find the longest exact prefix we can match
        match_len = 0
        while match_len < n and freq[ord(target[match_len]) - ord('a')] > 0:
            freq[ord(target[match_len]) - ord('a')] -= 1
            match_len += 1
            
        # Step 3: Backtrack to find the first place we can place a strictly greater character
        start_i = match_len
        
        # If we perfectly matched the entire target, we can't place a char at index n.
        # We must start backtracking at n - 1 and put that char back into our pool first.
        if start_i == n:
            start_i = n - 1
            freq[ord(target[start_i]) - ord('a')] += 1
            
        for i in range(start_i, -1, -1):
            target_char_idx = ord(target[i]) - ord('a')
            
            # Look for the smallest available character strictly greater than target[i]
            bump_char_idx = -1
            for j in range(target_char_idx + 1, 26):
                if freq[j] > 0:
                    bump_char_idx = j
                    break
                    
            if bump_char_idx != -1:
                # We found a valid character to "bump" up
                res = list(target[:i]) # 1. The exact prefix
                
                # 2. Append the bump character
                res.append(chr(bump_char_idx + ord('a')))
                freq[bump_char_idx] -= 1
                
                # 3. Collect and sort the remaining characters
                for k in range(26):
                    res.extend([chr(k + ord('a'))] * freq[k])
                
                return "".join(res)
            
            # If we couldn't bump at index i, we prepare for the next backtrack step (i - 1)
            # by putting target[i-1] back into our available frequency pool.
            if i > 0:
                freq[ord(target[i-1]) - ord('a')] += 1

        return ""
