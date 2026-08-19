class Solution:

    def encode(self, strs: List[str]) -> str:
        # append the string with its length and a delimeter 
        if not strs:
            return ""
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        i=0
        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            i = j+length+1
        return res

