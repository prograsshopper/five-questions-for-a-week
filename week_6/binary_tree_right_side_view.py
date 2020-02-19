# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rightSideView(self, root):
        result = []
        if not root:
            return result
        result.append(root.val)
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        result = result + right + left[len(right):]
        return result