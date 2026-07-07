class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        dict = {}
        round = 0

        for task in tasks:
            if task in dict:
                dict[task] += 1
            else:
                dict[task] = 1

        for freq, count in dict.items():
            if count == 1:
                return -1
            
            round += (count + 2) // 3

        return round
