class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = s.casefold()

        result = []
        for i in s2:
            if i.isalnum():
                result.append(i)
        
        rev = list(reversed(result))

        if rev != result:
            return False

        return True