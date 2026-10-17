class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def rec(nums: List[int]) -> List[List[int]]:
            if len(nums) == 1:
                return [[], [nums[0]]]
            num = nums[0]

            res = rec(nums[1:])
            res_extend = [lst + [num] for lst in res]
            return res + res_extend
        
        return rec(nums)