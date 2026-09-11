# Definition for a binary tree node.
from collections import deque

from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        que = deque()
        que.append(root)
        lx = 0
        ly = 0
        level = 0
        while que:
            size = len(que)
            level += 1
            for _ in range(size):
                cur = que.popleft()

                # 넣을때 검사하기
                if cur.left and cur.right:  # noqa: SIM102
                    if {cur.left.val, cur.right.val} == {x, y}:
                        return False  # 같은 부모라서 조카가 아님
                 
                # 현재 노드가 x인지 y인지 체크
                if cur.val == x:
                    lx = level
                if cur.val == y:
                    ly = level

                # 자식은 항상 넣기
                if cur.left:  que.append(cur.left)
                if cur.right: que.append(cur.right)

            # for문이 끝났을때 즉 같은 레벨일때 둘다 값이 있으면 return True
            if lx and ly:
                return True
            elif lx or ly:
                return False
        return False

