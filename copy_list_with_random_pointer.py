# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None
        inserted = self.insert(head)
        cp_list = self.copy_random(inserted)
        return self.split(cp_list)

    def insert(self, head):
        cur = head
        while cur != None:
            next = cur.next
            copy_cur = RandomListNode(cur.label)
            cur.next = copy_cur
            copy_cur.next = next
            cur = next
        return head

    def copy_random(self, head):
        cur = head
        while cur != None:
            copy_cur = cur.next
            if cur.random != None:
                copy_cur.random = cur.random.next
            else:
                copy_cur.random = None
            cur = copy_cur.next
        return head

    def split(self, head):
        head2 = head.next
        cur1 = head
        cur2 = RandomListNode(-1)
        cur2.next = head
        while cur1 != None:
            cur2.next = cur1.next
            cur2 = cur1.next
            cur1.next = cur2.next
            cur1 = cur1.next
        return head2
