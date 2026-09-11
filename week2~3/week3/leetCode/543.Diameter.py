# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: [TreeNode]) -> int: # type: ignore
        # 트리에서 아무 노드 두 개를 골라서 그 사이 경로의 엣지 수를 재. 가능한 모든 쌍 중 가장 긴 경로 = 지름.
        max_diameter = 0
        def high(root: [TreeNode]): # type: ignore
            nonlocal max_diameter
            if root is None:
                return -1
            left = high(root.left)+1
            right = high(root.right)+1

            max_diameter = max(max_diameter, left+right)
            return max(left, right)

        high(root)

        return max_diameter