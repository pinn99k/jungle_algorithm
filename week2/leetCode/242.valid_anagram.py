class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        if len(s) != len(t):
            return False

        for c in s:
            dic[c] = dic.get(c,0) + 1
        for c in t:
            dic[c] = dic.get(c,0) - 1

        for d in dic.values():
            if d != 0:
                return False

        return True