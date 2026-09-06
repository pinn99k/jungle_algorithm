from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def isMirror(n1, n2):
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None:
                return False

            return (
                (n1.val == n2.val)
                and isMirror(n1.left, n2.right)
                and isMirror(n1.right, n2.left)
            )

        # 보조 함수 호출
        return isMirror(root.left, root.right)