class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        _max_so_far = 0
        _streak = 0

        for num in nums:
            if num == 1:
                _streak += 1
            else:
                _max_so_far = max(_max_so_far, _streak)
                _streak = 0
        
        _max_so_far = max(_max_so_far, _streak)

        return _max_so_far