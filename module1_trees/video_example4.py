from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Main function to check if subRoot is a subtree of root.
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case: if subRoot is None, it is a subtree.
        if subRoot is None:
            return True

        # Base case: if root is None, subRoot can't be a subtree of root.
        if root is None and subRoot is not None:
            return False

        # Check if the current tree is the same as subRoot.
        if self.isSameTree(root, subRoot):
            return True

        # Recursively check left and right subtrees.
        left_check = self.isSubtree(root.left, subRoot)
        right_check = self.isSubtree(root.right, subRoot)

        return left_check or right_check

    # Helper function to check if two trees are identical
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: if both trees are empty
        if p is None and q is None:
            return True

        # Trees are not the same if either of them is empty or values are different
        if p is None or q is None or p.val != q.val:
            return False

        # Check recursively for left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
