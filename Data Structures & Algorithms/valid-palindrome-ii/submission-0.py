class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for char in range(len(s)):
            new_str = s[0:char] + s[char + 1:]
            if new_str == new_str[::-1]:
                return True
        return False
