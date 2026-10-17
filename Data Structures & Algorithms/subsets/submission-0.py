class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def rec(nums: List[int]) -> List[List[int]]:
            if len(nums) == 1:
                return [[], [nums[0]]]
            num = nums[0]

            res = rec(nums[1:])
            print(res, num)
            res_extend = [lst + [num] for lst in res]
            print(res_extend)
            return res + res_extend
        
        return rec(nums)