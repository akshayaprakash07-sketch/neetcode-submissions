class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        parathesis={')':'(',']':'[','}':'{'}
        for i in s:
            if i in parathesis:
                if stack and stack[-1]==parathesis[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
