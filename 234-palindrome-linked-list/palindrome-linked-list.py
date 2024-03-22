# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        string = ""
        curr = head
        while curr is not None:
            string += str(curr.val)
            curr = curr.next
        return string == string[::-1]
        
        