class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        stack_asterisk=[]
        dummy=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]=='*':
                stack_asterisk.append(i)
            else:
                if stack:
                    stack.pop()
                elif stack_asterisk:
                    stack_asterisk.pop()
                else:
                    return False
        
        while stack:
            if stack_asterisk:
                if stack_asterisk[-1]>stack[-1]:
                     stack_asterisk.pop()
                     stack.pop()
                else:
                    return False
            else:
                return False
        return True
