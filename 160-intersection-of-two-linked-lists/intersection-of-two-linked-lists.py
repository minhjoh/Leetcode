# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        currA, currB = headA, headB
        arrA = []
        arrB = []
        while currA:
            arrA.append(currA)
            currA = currA.next
        while currB:
            arrB.append(currB)
            currB = currB.next
        result = None
        while len(arrA) > 0 and len(arrB) > 0:
            tempA = arrA.pop()
            tempB = arrB.pop()
            if tempA != tempB:
                return result
            else:
                result = tempA
        return result
    