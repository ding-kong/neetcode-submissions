class Solution:
    def climbStairs(self, n: int) -> int:
        mem = defaultdict()
        mem[1] = 1
        mem[2] = 2

        def rec(nums: int) -> int:
            if nums < 3:
                return mem[nums]
            if nums in mem:
                return mem[nums]

            res = rec(nums-1) + rec(nums-2)
            mem[nums] = res
            return res
        
        return rec(n)
