class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [2,4,6]
        # going right: [  2,  8, (1)]
        # going left:  [(1), 24,  6 ]
        #              {r(i-1), out:1} * {l(i+1), out:1}
        going_right = []
        len_nums = len(nums)

        acc = 1
        for i, val in enumerate(nums):
            if i == len_nums:
                going_right.append(1)
                break
            acc *= val
            going_right.append(acc)
        
        going_left = [1] * len_nums
        acc = 1
        for i in range(len_nums - 1, 0, -1):
            val = nums[i]
            acc *= val
            going_left[i] = acc
        
        res = [1] * len_nums

        res[0] = going_left[1]
        res[len_nums-1] = going_right[len_nums-2]
        
        for i in range(1, len_nums-1):
            res[i] = going_right[i-1] * going_left[i+1]
        
        return res
        