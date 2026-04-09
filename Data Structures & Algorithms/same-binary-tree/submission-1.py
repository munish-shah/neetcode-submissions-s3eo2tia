# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        # Case 2: one is None, the other is not
        if p is None or q is None:
            return False

        # Case 3: both exist, but values are different
        if p.val != q.val:
            return False

        # At this point, p and q both exist and have the same value
        # Check left subtrees
        left_same = self.isSameTree(p.left, q.left)

        # Check right subtrees
        right_same = self.isSameTree(p.right, q.right)

        # Trees are the same only if both subtrees are the same
        return left_same and right_same