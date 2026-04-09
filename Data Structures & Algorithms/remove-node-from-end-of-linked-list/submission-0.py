# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        remove = head
        end = head

        count = 0
        while count != n:
            if end.next:
                end = end.next
            
            else:
                if remove.next:
                    head = head.next
                else:
                    head = None

                return head
            count += 1

        while end.next:
            end = end.next
            remove = remove.next
        

        remove.next = remove.next.next
            
        print(remove.val, end.val)

        return head