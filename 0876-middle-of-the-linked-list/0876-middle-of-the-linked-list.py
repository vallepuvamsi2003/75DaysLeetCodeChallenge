class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        temp = head
        
        while temp:
            count += 1
            temp = temp.next
        
        mid = count // 2
        temp = head
        
        for _ in range(mid):
            temp = temp.next
        
        return temp
        