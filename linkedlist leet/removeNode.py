# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        head = reverse(head)
        curr = head
        max_val = curr.val
        while curr and curr.next:
            if curr.next.val < max_val:
                curr.next = curr.next.next
            else:
                max_val = curr.next.val
                curr = curr.next
        return reverse(head)
