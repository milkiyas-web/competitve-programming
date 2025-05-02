# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp = []
        for i, node in enumerate(lists):
            if node:
                heappush(hp, (node.val, i, node))
        dummy = ListNode()
        curr = dummy
        while hp:
            val, i, node = heappop(hp)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heappush(hp, (node.val, i ,node))
        return dummy.next



