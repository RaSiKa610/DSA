import collections

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        # Dictionary to store the reserved seats for each row
        # Key: row number, Value: set of reserved seat numbers
        seats = collections.defaultdict(set)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9: # We only care about seats 2 through 9
                seats[row].add(seat)
        
        # Start by assuming all rows are completely empty
        # An empty row can fit exactly 2 families
        max_families = n * 2
        
        for row in seats:
            reserved = seats[row]
            
            # Since this row has reservations, remove the 2 families we initially counted
            max_families -= 2
            
            # Check availability of the three valid blocks
            left_available = not (reserved & {2, 3, 4, 5})
            right_available = not (reserved & {6, 7, 8, 9})
            middle_available = not (reserved & {4, 5, 6, 7})
            
            if left_available and right_available:
                max_families += 2
            elif left_available or right_available or middle_available:
                max_families += 1
                
        return max_families
