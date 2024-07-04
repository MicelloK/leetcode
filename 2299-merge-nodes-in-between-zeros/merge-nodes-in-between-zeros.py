# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node != None and node.next != None:
            if node.next.val == 0:
                if node.next.next == None:
                    node.next = None
                node = node.next
            else:
                node.val += node.next.val
                node.next = node.next.next
            
        return head