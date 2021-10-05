# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def FindKthToTail(self , pHead , k ):
        head,tail = pHead,pHead

        for i in range(k):
            if(tail!=None):
                tail = tail.next
            else:
                return None

        while(tail!=None):
            head = head.next
            tail = tail.next
        return head