class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
    
        # Find characters with odd frequency
        odd_chars = [ch for ch, count in freq.items() if count % 2 != 0]
        
        if len(odd_chars) > 1:
            return "IMPOSSIBLE"
        
        middle = odd_chars[0] if odd_chars else ""
        half = []
        
        # Sort characters for lexicographic order
        for ch in sorted(freq.keys()):
            half.append(ch * (freq[ch] // 2))
        
        left = "".join(half)
        right = left[::-1]
        
        return left + middle + right
