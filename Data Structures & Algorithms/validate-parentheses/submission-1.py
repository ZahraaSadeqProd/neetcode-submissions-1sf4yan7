class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchingLeftSide = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }

        for char in s:
            if len(stack) != 0 and char == matchingLeftSide[stack[len(stack)-1]]:
                stack.pop()
            else:
                if char not in matchingLeftSide:
                    return False
                stack.append(char)
            print(stack)
        return (len(stack) == 0)
        