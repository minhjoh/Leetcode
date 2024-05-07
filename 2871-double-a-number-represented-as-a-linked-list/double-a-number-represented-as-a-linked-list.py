# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def doubleString(self, string):
        carry = 0
        res = ""
        for i in range(len(string) - 1, -1, -1):
            doubleDigit = int(string[i]) * 2 + carry
            res += str(doubleDigit % 10)
            carry = doubleDigit // 10
        
        if carry:
            res += "1"

        return res[::-1]

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        string = ""
        curr = head
        while curr:
            string += str(curr.val)
            curr = curr.next
        
        string = self.doubleString(string)
        
        dummy_head = ListNode()
        curr = dummy_head

        for digit in string:
            curr.next = ListNode(int(digit))
            curr = curr.next
        
        return dummy_head.next

        
        
        
            

            
        

        