# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        sz = 0
        curr = head
        while curr:
            sz += 1
            curr = curr.next
        i = sz - n
        curr = head 
        if i == 0:
            head = curr.next
            return head
        elif i == sz - 1:
            while curr.next is not None:
                prev = curr
                curr = curr.next
            prev.next = None
            return head
        else:
            while i > 0:
                prev = curr
                curr = curr.next
                i = i - 1
            prev.next = curr.next
            return head

        