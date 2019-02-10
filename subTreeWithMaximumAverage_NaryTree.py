def findSubtree(root):
    s = Solution()
    s.findSubtree2(root)
    return s.node

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

class NaryTreeNode:
    def __init__(self,
                 val=None, children=None):
        self.val = val
        if not children:
            self.children = []
        else:
            self.children = children[:]


if __name__ == '__main__':
    NaryTreeNode_110 = NaryTreeNode(110)
    NaryTreeNode_20 = NaryTreeNode(20)
    NaryTreeNode_30 = NaryTreeNode(30)
    NaryTreeNode_120 = NaryTreeNode(120, [NaryTreeNode_110, NaryTreeNode_20, NaryTreeNode_30])


    NaryTreeNode_150 = NaryTreeNode(150)
    NaryTreeNode_80 = NaryTreeNode(80)
    NaryTreeNode_180 = NaryTreeNode(180, [NaryTreeNode_150, NaryTreeNode_80])

    NaryTreeNode_200 = NaryTreeNode(200, [NaryTreeNode_120, NaryTreeNode_180])
    findSubtree(NaryTreeNode_200)
