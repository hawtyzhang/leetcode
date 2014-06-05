# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        fast, slow = head, head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        second_head = slow.next
        slow.next = None
        head = self.sortList(head)
        second_head = self.sortList(second_head)
        return self.merge(head, second_head)

    def merge(self, head1, head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        if head1.val < head2.val:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next
        current = head
        while head1 != None and head2 != None:
            if head1.val < head2.val:
                current.next, head1 = head1, head1.next
            else:
                current.next, head2 = head2, head2.next
            current = current.next
        if head1 != None:
            current.next = head1
        elif head2 != None:
            current.next = head2
        return head

    def print_list(self, head):
        while head != None:
            print head.val,
            head = head.next
        print

vals = [1 for i in range(1000)]
node = None
for v in vals:
    current = ListNode(v)
    current.next = node
    node = current
s = Solution()
head = s.sortList(current)
s.print_list(head)
