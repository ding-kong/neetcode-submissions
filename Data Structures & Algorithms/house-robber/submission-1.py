class Solution:
    def rob(self, nums: List[int]) -> int:
        def rec(lst: List[int]) -> [int, int]: # with/without last house
            if len(lst) == 1:
                return [lst[0], 0]
            w, wout = rec(lst[1:])
            return (wout+lst[0], max(wout, w))
        return max(rec(nums))