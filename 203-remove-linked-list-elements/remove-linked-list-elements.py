# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curr_node, prev_node = head, None
        
        while curr_node:
            if curr_node.val == val:
                # need to delete current node
                if curr_node == head:
                    curr_node = head = head.next
                else:
                    prev_node.next = curr_node.next
                    curr_node = curr_node.next
            else:
                # go next
                prev_node = curr_node
                curr_node = curr_node.next

        return head