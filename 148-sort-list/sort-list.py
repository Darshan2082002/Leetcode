# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        # Base case: if list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Step 1: Split the list into two halves using the slow/fast pointer technique
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Cut the first half from the second half
        prev.next = None
        
        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(slow)
        
        # Step 3: Merge the two sorted halves
        return self.merge(left, right)

    def merge(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        # Attach the remaining nodes
        tail.next = l1 if l1 else l2
        return dummy.next