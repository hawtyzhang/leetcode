# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        return self.subtree_sum(0, root, sum)

    def subtree_sum(self, above, root, sum):
        if root.left == None and root.right == None:
            if root.val + above == sum:
                return True
            else:
                return False
        if root.left == None:
            return self.subtree_sum(above+root.val, root.right, sum)
        if root.right == None:
            return self.subtree_sum(above+root.val, root.left, sum)
        return self.subtree_sum(above+root.val, root.left, sum) or self.subtree_sum(above+root.val, root.right, sum)
