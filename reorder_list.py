# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None or head.next == None:
            return head
        head1, head2 = self.split(head)
        head2 = self.reverse(head2)
        return self.merge(head1, head2)

    def split(self, head):
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        second_head = slow.next
        slow.next = None
        return (head, second_head)

    def reverse(self, head):
        pre = None
        cur = head
        while cur.next != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        cur.next = pre
        return cur

    def merge(self, head1, head2):
        p1, p2 = head1, head2
        while p2 != None:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2
        return head1

    def print_list(self, head):
        while head != None:
            print head.val,
            head = head.next
        print 

nodes = [3, 2, 1]
next = None
for i in nodes:
    node = ListNode(i)
    node.next = next
    next = node
s = Solution()
result = s.reorderList(node)
s.print_list(result)
