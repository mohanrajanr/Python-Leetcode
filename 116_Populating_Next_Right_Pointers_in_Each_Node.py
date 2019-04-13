# # # # -*- coding: utf-8 -*-
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        if root.left and root.right:
            root.left.next = root.right
        if root.next and root.right:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        # incorrect if put here! why?
        # if root.next and root.right:
        #     root.right.next = root.next.left
        return root

if __name__ == '__main__':
    s = Solution()
    """
                              1
                     /                 \
                 2                           3
            /        \                     /    \
           4          5                   6      7
          / \       /   \               /   \   /  \
         8   9     10    11            12   13  14  15
    """
    # When dealing with 8->9, 10->11, because 5 is not connected to 6 yet, so 11 won't connect to 12