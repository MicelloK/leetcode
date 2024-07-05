# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        node = head.next
        i = 0
        min_idx = None
        max_idx = None
        min_dist = None
        while node.next != None:
            critical = node.val > prev.val and node.val > node.next.val or node.val < prev.val and node.val < node.next.val
            if critical:
                if min_idx == None:
                    min_idx = i
                if min_dist == None and max_idx != None:
                    min_dist = i - max_idx
                if max_idx != None:
                    min_dist = min(min_dist, i - max_idx)
                max_idx = i

            prev = node
            node = node.next
            i += 1

        if min_dist and min_dist > 0:
            return [min_dist, max_idx - min_idx]
        else:
            return [-1, -1]
        