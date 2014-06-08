# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root == None:
            return 0
        path = self.pathNum(root)
        return sum([int(i) for i in path])
    
    def pathNum(self, node):
        if node.left == None and node.right == None:
            return [str(node.val)]
        if node.left == None:
            return [str(node.val) + i for i in self.pathNum(node.right)]
        if node.right == None:
            return [str(node.val) + i for i in self.pathNum(node.left)]
        return [str(node.val) + i for i in self.pathNum(node.left)] + [str(node.val) + i for i in self.pathNum(node.right)]
