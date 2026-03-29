class Solution:
    def isValid(self, s: str) -> bool:
        closingParenthesis = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        if not s or len(s) == 0:
            return False

        stack = []

        for p in s:
            if p in closingParenthesis:
                if stack and stack[-1] == closingParenthesis[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
                
        return len(stack) == 0