# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1=self.reverseList(l1)
        l2=self.reverseList(l2)
        curr=l1
        num1=""
        while curr:
            num1+=str(curr.val)
            curr=curr.next
        curr=l2
        num2=""
        while(curr):
            num2+=str(curr.val)
            curr=curr.next
        ans=int(num1)+int(num2)
        dummy=ListNode()
        if ans==0:
            return dummy
        curr=dummy
        while(ans!=0):
            curr.next=ListNode(ans%10)
            ans=ans//10
            curr=curr.next
        return dummy.next





