class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set()
        res = 0
        for val in nums:
            st.add(val)
        print(st)

        for i in nums:
            if i-1 not in st and i in st:
                cur = i
                cnt = 0
                while cur in st:
                    cnt += 1
                    cur+= 1
                res = max(res, cnt)
        return res    