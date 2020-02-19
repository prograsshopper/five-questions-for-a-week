# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    result_sum = 0
    
    def rangeSumBST(self, root, L, R):
        if not root:
            return self.result_sum
        if L <= root.val <= R:
            self.result_sum += root.val
        self.rangeSumBST(root.right, L, R)
        self.rangeSumBST(root.left, L, R)
        return self.result_sum
