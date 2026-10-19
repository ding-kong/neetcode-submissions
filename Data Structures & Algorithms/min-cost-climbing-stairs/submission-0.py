class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c_minus_1, c_minus_2 = 0, 0

        for i, c in enumerate(cost):
            # print("begin", i, c, c_minus_1, c_minus_2)
            c_minus_1, c_minus_2 = min(c_minus_1 + c, c_minus_2 + c), c_minus_1
            # print("end", i, c, c_minus_1, c_minus_2)
        
        return min(c_minus_1, c_minus_2)