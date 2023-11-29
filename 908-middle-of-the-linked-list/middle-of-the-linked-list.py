# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count, i = 0, 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        while i < int(count/2):
            head = head.next
            i += 1
        return head