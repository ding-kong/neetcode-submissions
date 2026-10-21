class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        if len(num_set) <= 0:
            return 0
        
        _max = 1

        for num in num_set:
            if num - 1 in num_set:
                continue
            
            current_seq = 1
            
            while num + current_seq in num_set:
                current_seq += 1
            
            _max = max(_max, current_seq)
        
        return _max