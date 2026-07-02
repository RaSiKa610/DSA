# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k== 0:
            return head
        p = head
        i = 1
        while p.next:
            p = p.next
            i += 1

        k %= i

        if k == 0:
            return head

        q = head
        p.next = q
        step = i - k - 1
        while step:
            q = q.next
            step -= 1
        newHead = q.next
        q.next = None

        return newHead
            
