class Solution:
    def isPalindrome(self,s: str) -> bool:
        clean_text = "".join([char.lower() for char in s if char.isalnum()])
        t = clean_text[::-1]
        if clean_text == t:
            return True
        else:
            return False

        