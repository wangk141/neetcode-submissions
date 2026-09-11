class Solution:
    def isPalindrome(self, s: str) -> bool:
        twoString = ""
        for letter in s:
            if letter.isalnum():
                twoString += letter
        return twoString.lower() == twoString[::-1].lower()