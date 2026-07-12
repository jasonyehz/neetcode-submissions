class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        # s = "([{}])"
        for char in s:
            # Goes through string and if the char is in pairs, which means it's a closing bracket
            # Else if it's opening, just append.
            # Now that we see it's a closing bracket, check stack[-1] to see if it's the corresponding value
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                else:
                    stack.pop()
            else: 
                stack.append(char)

        if not stack:
            return True

        else: return False 
        



        

