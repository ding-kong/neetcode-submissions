class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        elif n <=2:
            return 2
        
        minus_2 = 1
        minus_1 = 2

        for _ in range(n-2):
            minus_2, minus_1 = minus_1, minus_1 + minus_2
        
        return minus_1

    def topDownClimbStairs(self, n: int) -> int:
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
