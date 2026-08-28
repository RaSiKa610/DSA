import collections

class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        counts = collections.Counter(s)
        
        # 1. Base check: Can we even form a palindrome?
        odd_count = sum(1 for v in counts.values() if v % 2 != 0)
        if odd_count > (1 if n % 2 != 0 else 0):
            return ""
            
        half_len = n // 2
        
        # 2. Check if an exact match of target's first half works and naturally beats target
        def check_exact():
            c_copy = counts.copy()
            prefix = []
            for k in range(half_len):
                char = target[k]
                if c_copy[char] < 2: return ""
                c_copy[char] -= 2
                prefix.append(char)
            
            mid = ""
            if n % 2 != 0:
                char = target[half_len]
                if c_copy[char] < 1: return ""
                c_copy[char] -= 1
                mid = char
                
            res = "".join(prefix) + mid + "".join(prefix)[::-1]
            if res > target:
                return res
            return ""
        
        res = check_exact()
        if res: 
            return res
        
        # 3. Try to diverge at index i (iterate from highest index down to 0 to keep the longest prefix)
        max_i = (n - 1) // 2
        
        for i in range(max_i, -1, -1):
            c_copy = counts.copy()
            possible_to_match = True
            prefix = []
            
            # Lock in the prefix matching target[0...i-1]
            for k in range(i):
                char = target[k]
                if c_copy[char] < 2:
                    possible_to_match = False
                    break
                c_copy[char] -= 2
                prefix.append(char)
            
            if not possible_to_match:
                continue
                
            # Diverge at index i with a strictly greater character
            start_char = chr(ord(target[i]) + 1)
            
            for cand_ord in range(ord(start_char), ord('z') + 1):
                cand = chr(cand_ord)
                
                if i == half_len: 
                    # Odd-length string, and we are diverging at the exact middle character
                    if c_copy[cand] >= 1:
                        return "".join(prefix) + cand + "".join(prefix)[::-1]
                else:
                    # Diverging somewhere in the first half
                    if c_copy[cand] >= 2:
                        c_copy2 = c_copy.copy()
                        c_copy2[cand] -= 2
                        
                        mid_char = ""
                        if n % 2 != 0:
                            # Reserve the single remaining odd-count character for the middle
                            for ch, v in c_copy2.items():
                                if v % 2 != 0:
                                    mid_char = ch
                                    c_copy2[ch] -= 1
                                    break
                                    
                        # Greedily fill the remaining first-half slots with the smallest available pairs
                        rest_prefix = []
                        for ch_ord in range(ord('a'), ord('z') + 1):
                            ch = chr(ch_ord)
                            while c_copy2[ch] >= 2:
                                rest_prefix.append(ch)
                                c_copy2[ch] -= 2
                                
                        full_prefix = "".join(prefix) + cand + "".join(rest_prefix)
                        return full_prefix + mid_char + full_prefix[::-1]
        
        return ""
