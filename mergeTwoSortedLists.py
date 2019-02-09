# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        head = l1 if l1.val <= l2.val else l2
        p1 = l1.next if l1.val <= l2.val else l1
        p2 = l2.next if l2.val < l1.val else l2

        p = head

        while (p1 and p2):
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        else:
            p.next = p2
        return head
