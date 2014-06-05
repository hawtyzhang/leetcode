# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        result = []
        stack = []
        if root != None:
            stack.append(root)
        while len(stack):
            last = stack.pop()
            if isinstance(last, TreeNode):
                stack.append(last.val)            
                if last.right:
                    stack.append(last.right)
                if last.left:
                    stack.append(last.left)
            else:
                result.append(last)
        return result
