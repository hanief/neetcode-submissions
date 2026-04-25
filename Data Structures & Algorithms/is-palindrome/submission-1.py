class Solution:
    def isPalindrome(self, s: str) -> bool:
        ori = "".join(char for char in s if char.isalnum()).lower()
        rev = ori[::-1]

        return rev == ori