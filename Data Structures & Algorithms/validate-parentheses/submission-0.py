class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for p in s:
            if p in open_to_close:
                stack.append(p)
            else:
                if stack:
                    p2 = stack.pop()
                    if p != open_to_close[p2]:
                        return False
                else:
                    return False
        
        return len(stack) == 0

