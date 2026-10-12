class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        # store remaining amount to index
        # look for the coming amount in the dict
        for index, num in enumerate(nums):
            if num in d:
                return [d[num], index]
            d[target-num] = index
        return [0,1]