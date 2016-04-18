# # # # -*- coding: utf-8 -*-
# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
            return head
        if head is None:
            return head
        old_head = head
        # get tail
        tail = head
        length = 1
        while tail.next:
            length += 1
            tail = tail.next

        k = k % length
        if k == 0:
            return head

        start = head
        prev = None

        i = 0
        while i < length - k:
            prev = start
            start = start.next
            i += 1
        prev.next = None
        new_head = start

        tail.next = old_head
        return new_head

    def printList(self,head):
        temp = head
        while temp is not None:
            print temp.val
            temp = temp.next
        return

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    # l3.next = l4
    # l4.next = l5
    head = l1
    k = 2000000000
    #k = 2
    new_head = s.rotateRight(l1,k)
    s.printList(new_head)