# Objective: Determine the max depth of a binary tree given its root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left) # Recursive DFS
        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth) # Add 1 to the maximum depth found on either side
