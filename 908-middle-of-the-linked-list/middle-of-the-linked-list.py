# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail=head
        count=0
        while tail:
            count+=1
            tail=tail.next
       
        
        if count==0:
            return head
        
        temp=0
        tail=head
        print(count)
        while temp!=count//2:
            temp+=1
            tail=tail.next
        
        return tail


