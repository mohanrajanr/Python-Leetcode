class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree
    average, node = 0, None

    def findSubtree2(self, root):
        # Write your code here
        self.helper(root)
        return self.node

    def helper(self, root):
        if root is None:
            return 0, 0

        sum = root.val
        size = 1
        for c in root.children:
            temp_sum, temp_size = self.helper(c)
            sum += temp_sum
            size += temp_size

        if self.node is None or sum * 1.0 / size > self.average:
            self.node = root
            self.average = sum * 1.0 / size

        return sum, size

