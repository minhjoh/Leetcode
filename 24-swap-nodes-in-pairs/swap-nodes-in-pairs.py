# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr is not None and curr.next is not None:
            temp = curr.val
            curr.val = curr.next.val
            curr.next.val = temp
            curr = curr.next.next
        return head