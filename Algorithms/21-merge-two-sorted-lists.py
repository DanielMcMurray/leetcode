# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        temp = current = ListNode(0)
        temp.next = list1
        while list1 and list2:
            if list1.val < list2.val:
                list1 = list1.next
            else:
                next = current.next
                current.next = list2
                t = list2.next
                list2.next = next
                list2 = t
            current = current.next
        current.next = list1 or list2
        return temp.next

    mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4])
