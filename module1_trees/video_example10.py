from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0

            # Recursive call on left and right child
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Update max_sum if it's better to start a new path
            price_newpath = node.val + left_gain + right_gain
            max_sum = max(max_sum, price_newpath)

            # For recursion return dfs if continue the same path
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return max_sum
