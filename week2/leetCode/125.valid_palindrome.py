class Solution:
    def isPalindrome(self, s: str) -> bool:

        rev_str = ""

        for c in s:
            if c.isalnum():
                rev_str += c.upper()
        return rev_str == rev_str[::-1]
