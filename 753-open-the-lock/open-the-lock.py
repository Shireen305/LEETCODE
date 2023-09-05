class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        def children (wheel):
            res=[]
            for i in range(4):
                digit=str((int(wheel[i])+1)%10)
                res.append(wheel[:i]+digit+wheel[i+1:])
                digit = str((int(wheel[i]) + 10 - 1) % 10)
                res.append(wheel[:i] + digit + wheel[i + 1 :])
            return res
        queue=[('0000',0)]
        visit=set(deadends)
        while queue:
            wheel,turn=queue.pop(0)
            if wheel==target:
                return turn
            for child in children(wheel):
                if child not in visit:
                    visit.add(child)
                    queue.append((child,turn+1))
        return -1

                



        