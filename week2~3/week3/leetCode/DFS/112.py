# Definition for a binary tree node.
from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 백트레킹 문제?
        # 내려가면서 더하고 되면 리턴 안되면 이전값 복구
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum

        return bool(self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val))

