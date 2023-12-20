# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        li = []
        curr = head
        while curr is not None and curr.next is not None:
            if curr.next in li:
                return True
            li.append(curr.next)
            curr = curr.next
        return False
