# # # # -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            res = []
            self.dfs(root, res)
            print res
            dummy = TreeNode(0)
            prev = dummy
            curr = root
            for i in range(len(res)):
                if not curr:
                    curr = TreeNode(res[i])
                else:
                    curr.val = res[i]
                    curr.left = None
                prev.right = curr
                curr = curr.right
                prev = prev.right
    def dfs(self, root, res):
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)

if __name__ == '__main__':
    s = Solution()
    """
        1
       / \
      2   5
     / \   \
    3   4   6
    """
    left = TreeNode(2, TreeNode(3), TreeNode(4))
    right = TreeNode(5, None, TreeNode(6))
    root = TreeNode(1, left, right)
    s.flatten(root)