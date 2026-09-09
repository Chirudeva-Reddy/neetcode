class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        t = s[::-1].lower()
        if s.lower() == t:
            return True
        else:
            return False