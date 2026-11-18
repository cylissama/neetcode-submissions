class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """ItemsView, 
        Do not return anything, modify nums in-place instead.
        """
        # insertion sort
        for i in range(1, len(nums)):
            n = nums[i]
            p = i - 1

            while p >= 0 and nums[p] > n:
                nums[p + 1] = nums[p]
                p -= 1

            nums[p + 1] = n

