class Solution:
    def isValid(self, s: str) -> bool:
        para = {')':'(', '}':'{', ']':'['}
        stack = []

        for ch in s:
            if ch in para:
                if not stack or stack.pop() != para[ch]:
                    return False
        
            else:
                stack.append(ch)

        return not stack     