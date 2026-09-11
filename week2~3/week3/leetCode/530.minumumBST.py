# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    min_num = 0
    def getMinimumDifference(self, root: [TreeNode]) -> int: # type: ignore
        # 중위순회가 맞음
        # 왼쪽 중앙 오른쪽 순서
        # 왼쪽 아래부터 올라오면서 검사
        # 오른쪽으로 내려가면서 검사
        result = float('inf')
        prev = None
        # 뒤에 값이 없으면 리턴
        def search(root):
            nonlocal result, prev

            if root is None: return

            search(root.left)
            
            if prev is not None:
                result = min(result, abs(root.val - prev))
            prev = root.val

            search(root.right)
        # 루트 - 왼쪽 vs 루트 - 오른쪽 중 더 작은 값을 리턴

        search(root)
        return result