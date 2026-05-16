class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_letters=''
        for i in range(len(s)):
            if s[i].isalnum():
                only_letters+=s[i]
        if only_letters.lower()==only_letters[::-1].lower():
            return True
        else:
            return False