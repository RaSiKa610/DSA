# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        p = head
        i = 1

        while p.next is not None:
            i += 1
            p = p.next

        if n > i:
            return head

        if n == i:
            return head.next

        p = head
        x = i - n 
        while x > 1:
            p = p.next
            x -= 1

        p.next = p.next.next

        return head
            
