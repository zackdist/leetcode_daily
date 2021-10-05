# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        count =0
        while(n & 0xffffffff != 0):
            n = n & (n-1)
            count+=1
        return count

