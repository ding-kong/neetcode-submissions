class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        _min = min(nums)
        _len = len(nums)
        _set = set(nums)

        for num in range(_min, _min+_len):
            if num not in _set:
                return False
        return True