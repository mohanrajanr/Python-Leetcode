# # # # -*- coding: utf-8 -*-
"""
# Definition for singly-linked list.


Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
# https://blog.csdn.net/m0_37324740/article/details/80769702
import heapq

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        temp = ListNode(-1)
        head = temp
        while heap:
            smallestNode_val = heapq.heappop(heap)
            temp.next = ListNode(smallestNode_val)
            temp = temp.next

        return head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        heap_result = []
        node_dict = {}
        is_lists_empty = True
        while not is_lists_empty:
            is_lists_empty = True
            for i in range(len(lists)):
                remove_node = self.removeHead(i, lists)
                if remove_node:
                    is_lists_empty = False
                    heapq.heappush(heap_result, remove_node.val)
                    if remove_node.val not in node_dict:
                        node_dict[remove_node.val] = []
                    node_dict[remove_node.val].append(remove_node)

        dummy = ListNode(0)
        step = dummy
        while len(heap_result) > 0:
            val = heapq.heappop(heap_result)
            val_nodes = node_dict[val]
            for n in val_nodes:
                step.next = n
                step = step.next
        return dummy.next

    def removeHead(self, i, lists):
        # Remove the ith element's head in lists
        head = lists[i]
        if head:
            new_head = head.next
            lists[i] = new_head
            return head
        return None

if __name__ == '__main__':
    s = Solution()
    