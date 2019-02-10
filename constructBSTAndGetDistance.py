# # # # -*- coding: utf-8 -*-
class BTNode:
    """Binary Tree node."""
    def __init__(self, data, left=None, right=None):
        """Create BT node with data and children left and right.
        """
        self.data = data
        self.left = left
        self.right = right

def buildBSTFromArray(array, num1, num2):
    if num1 not in array or num2 not in array:
        return -1
    if len(array) == 0:
        return None
    root = BTNode(array[0])
    for num in array:
        insert(root, num)
    return root

def insert(bt, data):
    return_node = bt
    if bt is None:
        return_node = BTNode(data)
    elif data < bt.data:
        bt.left = insert(bt.left, data)
    elif data > bt.data:
        bt.right = insert(bt.right, data)
    return return_node

def distanceInBST(root, num1, num2):
    lowest = lowestCommonAncestorBST(root, num1, num2)
    return getDistance(lowest, num1) + getDistance(lowest, num2)

def getDistance(root, num):
    """ Given a root and a num in tree, find the distance between them """
    if num == root.data:
        return 0
    elif num < root.data:
        return 1 + getDistance(root.left, num)
    elif num > root.data:
        return 1 + getDistance(root.right, num)

def lowestCommonAncestorBST(root, num1, num2):
    if root.data == num1 or root.data == num2:
        return root
    elif root.data < num1 and root.data < num2:
        return lowestCommonAncestorBST(root.right, num1, num2)
    elif root.data > num1 and root.data > num2:
        return lowestCommonAncestorBST(root.left, num1, num2)
    else:
        return root


if __name__ == '__main__':
    array = [12, 5, 9, 4, 8, 10]
    num1 = 5
    num2 = 8
    root = buildBSTFromArray([12, 5, 9, 4, 8, 10], num1, num2)
    print(root)
    """
          12
         /
        5
       / \
      4   9
         / \
        8  10
    """

    print(distanceInBST(root, num1, num2))
    # TODO
