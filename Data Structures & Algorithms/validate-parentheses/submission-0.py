class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif stack and stack[-1]==mapping[i]:
                stack.pop()
            else:
                return False
        return not stack    