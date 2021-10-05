class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def Print(pRoot):
    # write code here
    if not pRoot:
        return []
    queue = [pRoot]
    outList = []
    while queue:
        res = []
        i = 0
        numberFlag = len(queue)  # 这一步记录当前层中节点的个数
        while i < numberFlag:  # 这里再遍历每一层
            point = queue.pop(0)
            res.append(point.val)
            if point.left:
                queue.append(point.left)
            if point.right:
                queue.append(point.right)
            i += 1
        outList.append(res)
    print(outList)

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pre int整型一维数组
# @param vin int整型一维数组
# @return TreeNode类
#
class Solution:
    def reConstructBinaryTree(self , pre, vin) :
        # write code here
        # pre: 前序
        # vin: 中序

        # 索引
        vin_dic = {}


        def get_tree_root(pre, vin):
            root_node = TreeNode(pre[0])
            root_index = vin.index(pre[0])

            # 左子树的节点数量
            left_num = root_index

            # 左右子树的前序与中序
            left_pre = pre[1:left_num+1]
            left_vin = vin[:root_index]

            right_pre = pre[left_num + 1:]
            right_vin = vin[root_index+1:]

            root_node.left = None
            root_node.right = None

            # 获得左右子树的根节点
            if(len(left_pre)!=0):
                root_node.left = get_tree_root(left_pre,left_vin)
            if(len(right_pre)!=0):
                root_node.right = get_tree_root(right_pre,right_vin)

            return root_node

        if(len(pre)==0):
            return None
        root_node = get_tree_root(pre,vin)
        return root_node

so = Solution()
# [1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]
pre = [3, 5, 6, 8]
tin = [5, 3, 8, 6]
root_node = so.reConstructBinaryTree(pre,tin)
Print(root_node)


