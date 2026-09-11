class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        arr = set()
        for i in nums:
            if i in arr:
                return True
            arr.add(i)

        return False