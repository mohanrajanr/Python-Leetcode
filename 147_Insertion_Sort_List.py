# # # # -*- coding: utf-8 -*-

# Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        while curr is not None:
            pre = dummy
            while pre.next is not None and pre.next.val < curr.val:
                pre = pre.next

            temp = curr.next
            curr.next = pre.next
            pre.next = curr
            curr = temp
        return dummy.next


if __name__ == '__main__':
    s = Solution()

    """
        33  44  11  22



        11  33  44  22
dummy
    """
    l4 = ListNode(22)
    l3 = ListNode(11)
    l3.next = l4
    l2 = ListNode(44)
    l2.next = l3
    l1 = ListNode(33)
    l1.next = l2
    head = l1
    s.insertionSortList(head)
