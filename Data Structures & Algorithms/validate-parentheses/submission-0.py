class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {"}":"{", ")":"(", "]": "["}
        for ch in s:
            print( pMap.get(ch))
            if len(stack) > 0 and stack[len(stack) -  1] == pMap.get(ch):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0