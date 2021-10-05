class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return TreeNode类
#
from queue import  Queue
class Solution:
    def Mirror(self , pRoot ):
        # write code here
        # 广度优先遍历

        queue = Queue(maxsize=0)
        queue.put(pRoot)
        if(pRoot==None):
            return None

        while(not queue.empty()):
            now = queue.get()

            tmp = now.left
            now.left = now.right
            now.right = tmp

            if(now.left!=None):
                queue.put(now.left)

            if(now.right!=None):
                queue.put(now.right)

        return pRoot