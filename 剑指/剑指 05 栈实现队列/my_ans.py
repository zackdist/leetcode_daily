# -*- coding:utf-8 -*-
# 栈是先进后出
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        while(len(self.stack2) !=0):
            item = self.stack2.pop()
            self.stack1.append(item)
        self.stack2.append(node)
        while (len(self.stack1) != 0):
            item = self.stack1.pop()
            self.stack2.append(item)

    def pop(self):
        item = self.stack2.pop()
        return item