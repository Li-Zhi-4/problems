class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) % 2 != 0:
            return False

        stack = []
        opening = ["[", "{", "("]
        mapping = {
            "[": "]",
            "{": "}",
            "(": ")",
            "]": "[",
            "}": "{",
            ")": "("
        }

        for br in s:
            if br in opening:
                stack.append(br)
            else:
                if not stack:
                    return False
                recent = stack.pop()
                if mapping[br] != recent:
                    return False
        
        return not stack



        