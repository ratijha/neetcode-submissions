class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wc1 = {}
        wc2 = {}
        if len(s) != len(t):
            return False
        for i in s:
            try:
                wc1[i] += 1
            except Exception:
                wc1[i] = 1
        for i in t:
            try:
                wc2[i] += 1
            except Exception:
                wc2[i] = 1

        if wc1 == wc2:
            return True
        else:
            return False