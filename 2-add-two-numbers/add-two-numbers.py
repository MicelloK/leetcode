# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        excess = 0
        while l1 and l2:
            tail.next = ListNode((l1.val + l2.val + excess) % 10)
            tail = tail.next
            excess = (l1.val + l2.val + excess) // 10
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            tail.next = ListNode((l1.val + excess) % 10)
            tail = tail.next
            excess = (l1.val + excess) // 10
            l1 = l1.next

        while l2:
            tail.next = ListNode((l2.val + excess) % 10)
            tail = tail.next
            excess = (l2.val + excess) // 10
            l2 = l2.next

        if excess:
            tail.next = ListNode(excess)
        
        return head.next
        
