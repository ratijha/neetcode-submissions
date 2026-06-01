class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        wc = {}
        for i in nums:
            try:
                wc[i] += 1
            except Exception:
                wc[i] = 1
        for i in nums:
            if wc[i]>1:
                return True
        else:
            return False
            

