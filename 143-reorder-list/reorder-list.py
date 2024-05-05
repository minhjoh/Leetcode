# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        left, right = 0, len(stack) - 1
        while left < right:
            temp = stack.pop()
            stack[-1].next = None
            curr = stack[left]
            temp.next = curr.next
            curr.next = temp
            right -= 1
            left += 1