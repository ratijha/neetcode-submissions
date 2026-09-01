class Solution:
    def isValid(self, s: str) -> bool:
        map = {"}": "{", ")": "(", "]":"["}
        if not s:
            return True
        stack = []
        for i in s:
            if i in map:
                ele = stack.pop() if stack else None
                if map[i] != ele:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0
                