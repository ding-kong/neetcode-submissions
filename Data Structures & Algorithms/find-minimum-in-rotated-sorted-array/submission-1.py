from bisect import bisect_left

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        i = bisect_left(nums, True, key=lambda v: v < nums[0])
        return nums[i]