import math
import copy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        prod = 1
        for i in nums:
            if i:
                prod *=i
            else:
                zero_cnt +=1
        if zero_cnt>1:
            res = [0]*len(nums)
        else:
            res = [0]*len(nums)
            for i,j in enumerate(nums):
                if zero_cnt:
                    res[i] = 0 if j else prod
                else:
                    res[i] = prod//j
        return res
