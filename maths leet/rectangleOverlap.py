class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # Check if either rectangle is actually a line/point (area = 0)
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or \
           rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
            
        # Return False if they don't overlap in any dimension
        if rec1[2] <= rec2[0] or \
           rec1[0] >= rec2[2] or \
           rec1[3] <= rec2[1] or \
           rec1[1] >= rec2[3]:
            return False
            
        return True
