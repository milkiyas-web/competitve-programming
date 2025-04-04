# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        
        def merge(left, right):
            dummy = ListNode(0)
            curr = dummy
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            if left:
                curr.next = left
             
            if right:
                curr.next = right
                
            return dummy.next

        def merge_sort(head):
            if not head or not head.next:
                return head 
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            left = merge_sort(head)
            right = merge_sort(mid)
            return merge(left, right)
        return merge_sort(head)


        