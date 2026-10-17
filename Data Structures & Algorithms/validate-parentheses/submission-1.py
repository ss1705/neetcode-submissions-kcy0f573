class Solution:
    def isValid(self, s: str) -> bool:
        para = {')':'(', '}':'{', ']':'['}
        stack = []

        for ch in s:
            if ch in para:
                if not stack:
                    return False
                candidate = stack.pop()
                if candidate != para[ch]:
                    return False
        
            else:
                stack.append(ch)

        return not stack     