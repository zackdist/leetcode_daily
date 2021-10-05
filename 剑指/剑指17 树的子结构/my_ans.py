# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from queue import Queue

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if(pRoot1==None or pRoot2==None):
            return False
        # 广度优先遍历
        queue = Queue(maxsize=0)
        queue.put(pRoot1)

        while(not queue.empty()):
            now = queue.get()
            if(now.val == pRoot2.val):
                if(self.is_same_tree(now,pRoot2)):
                    return True

            left = now.left
            right = now.right

            if left!=None:
                queue.put(left)
            if right!=None:
                queue.put(right)

        return False

    def is_same_tree(self,pRoot1,pRoot2):

        if(pRoot1==None and pRoot2==None):
            return True

        if(pRoot2==None):
            return True

        if(pRoot1==None):
            return False

        if(pRoot1.val == pRoot2.val):
            return self.is_same_tree(pRoot1.left,pRoot2.left) and self.is_same_tree(pRoot1.right,pRoot2.right)

        return False

pRoot1 = TreeNode(8)
pRoot1.left = TreeNode(8)
pRoot1.right = TreeNode(7)
pRoot1.left.left = TreeNode(9)
pRoot1.left.right = TreeNode(2)

pRoot2 = TreeNode(8)
pRoot2.left = TreeNode(9)
pRoot2.right = TreeNode(2)

so = Solution()
res = so.HasSubtree(pRoot1,pRoot2)
print(res)
