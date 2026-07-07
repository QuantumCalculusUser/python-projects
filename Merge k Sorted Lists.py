# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

# def startof(lists):
#     for node in lists:
#         if node:
#             return True
#     return False

# def smallest(lists):
#     smallest_val = float('inf')
#     smallest_idx = -1

#     for i, node in enumerate(lists):
#         if node and node.val < smallest_val:
#             smallest_val = node.val
#             smallest_idx = i

#     lists[smallest_idx] = lists[smallest_idx].next
#     return smallest_val


# class Solution(object):
#     def mergeKLists(self, lists):
#         dummy = ListNode(0)
#         current = dummy

#         while startof(lists):
#             val = smallest(lists)

#             current.next = ListNode(val)
#             current = current.next

#         return dummy.next