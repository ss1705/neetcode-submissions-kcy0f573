class Solution:
    def isValid(self, s: str) -> bool:
        para = {')':'(', '}':'{', ']':'['}
        stack = []

        for ch in s:
            if ch in para.values():
                stack.append(ch)
            
            else:
                if not stack:
                    return False

                candidate = stack.pop()
                if candidate != para[ch]:
                    return False

        return not stack     