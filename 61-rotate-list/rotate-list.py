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
        
        k %= size
        
        if k == 0:
            return head
        
        curr.next = head
        
        curr = head
        for _ in range(size - k - 1):
            curr = curr.next
        
        new_head = curr.next
        curr.next = None
        
        return new_head
        