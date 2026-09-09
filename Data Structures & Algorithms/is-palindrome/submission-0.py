class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        new = s.lower()
        #t = "".join(char for char in s[::-1] if char.isalnum())
        t = s[::-1].lower()
        if new == t:
            return True
        else:
            return False