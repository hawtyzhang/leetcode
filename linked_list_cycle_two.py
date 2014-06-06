# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        meet_point = self.hasCycle(head)
        if meet_point == None:
            return None
        p1, p2 = head, meet_point
        while p1 != p2:
            p1, p2 = p1.next, p2.next
        return p1

    def hasCycle(self, head):
        if head == None:
            return None
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return fast
        return None
