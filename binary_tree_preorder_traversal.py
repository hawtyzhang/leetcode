# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result = []
        stack = []
        if root != None:
            stack.append(root)
        while len(stack):
            last = stack.pop()
            if isinstance(last, TreeNode):
                if last.right:
                    stack.append(last.right)
                if last.left:
                    stack.append(last.left)
                stack.append(last.val)            
            else:
                result.append(last)
        return resultult.append(last)
        return result
