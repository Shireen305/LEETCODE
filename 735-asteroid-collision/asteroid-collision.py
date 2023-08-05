class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        stack.append(asteroids[0])
        for i in range(1,len(asteroids)):
            if stack and stack[-1]>0>asteroids[i]:
                while stack and stack[-1]>0>asteroids[i]:
                    if stack[-1]<abs(asteroids[i]):
                        stack.pop()
                    elif stack[-1]==abs(asteroids[i]):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(asteroids[i])     


            else:
                stack.append(asteroids[i])     
                #print(stack)   
        return stack
       