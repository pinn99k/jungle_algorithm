class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        f = 0
        e = n-1
        i = 0

        while i <= e:
            if nums[i] == 0:
                nums[f], nums[i] = nums[i], nums[f]
                i+=1
                f+=1
            elif nums[i] == 2:
                nums[e], nums[i] = nums[i], nums[e]
                e-=1
            else:
                i+=1
