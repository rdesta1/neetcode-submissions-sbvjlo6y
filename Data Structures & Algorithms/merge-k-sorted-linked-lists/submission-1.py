# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        
        if not lists:
            return ListNode(val='')
            
        arr = []
        
        for i in lists:
            cur = i
            while cur != None:
                arr.append(cur.val)
                cur = cur.next
        arr.sort()

        
        

        cur = ListNode(arr[0])
        head = cur

        for i in range(1, len(arr)):
            cur.next = ListNode(arr[i])
            cur = cur.next
        return head