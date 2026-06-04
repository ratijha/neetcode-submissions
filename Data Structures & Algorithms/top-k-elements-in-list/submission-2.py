class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        x =[]
        for i in nums:
            try:
                res[i] += 1
            except Exception as e:
                res[i] = 1
        
        y =  sorted(res, key=res.get, reverse=True)
        return y[:k]