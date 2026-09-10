# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if  not (list1 and list2):
            return list1 if list1 else list2

        res = list1 if list1.val < list2.val else list2
        new_list = res

        if list1 is res:
            list1 = list1.next
        else:
            list2 = list2.next

        while list1 and list2:
            if list1.val < list2.val:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            new_list = new_list.next
        
        new_list.next = list1 if list1 else list2
        
        return res

    