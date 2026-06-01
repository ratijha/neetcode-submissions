class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x,i in enumerate(nums):
            diff = target - i
            if diff in nums and nums.index(diff) != x:
                indices = [x,nums.index(diff)]
                indices.sort()
                return indices