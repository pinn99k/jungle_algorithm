class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        def search(left: int, right: int):
            if left > right:
                return -1
            mid = (right+left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return search(mid+1, right)
            elif nums[mid] > target:
                return search(left, mid-1)

        return search(0,n-1)