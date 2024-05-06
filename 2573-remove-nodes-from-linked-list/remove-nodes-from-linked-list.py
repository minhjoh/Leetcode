# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        ptr=head
        while ptr:
            arr.append(ptr.val)
            ptr=ptr.next
        
        mono=[]
        for num in arr:
            while(mono and num>mono[-1]):
                # print(arr)
                mono.pop()
            mono.append(num)
        
        node=ListNode(-1)
        ptr=node
        for i in mono:
            temp=ListNode(i)
            ptr.next=temp
            ptr=ptr.next

        return node.next