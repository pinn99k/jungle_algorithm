# Definition for a binary tree node.
from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 둘다 None 이면 True 임
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        if p.val != q.val:
            return False
        
        return bool(self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))