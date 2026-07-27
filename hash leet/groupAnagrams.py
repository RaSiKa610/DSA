
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        r = []
        hashmap = {}
        for word in strs:
            sorted_key = "".join(sorted(word))
            if sorted_key in hashmap:
                hashmap[sorted_key].append(word)
            else:
                hashmap[sorted_key] = [word]
        r = list(hashmap.values())

        return r
