# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        size, curr = 1, head
        while curr.next:
            size += 1
            curr = curr.next

        if k % size == 0:
            return head

        if k > size:
            k %= size
        
        curr.next = head
        curr = head
        i = 0
        steps = size - k - 1
        while i < steps:
            i += 1
            curr = curr.next
        start = curr.next
        curr.next = None
        return start
        