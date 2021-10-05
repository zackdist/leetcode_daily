# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        res =[]
        res.append(0)
        res.append(1)
        res.append(2)
        for i in range(3,number+1):
            res.append(res[i-1]+res[i-2])
        return res[number]
so = Solution()
num = so.rectCover(4)
print(num)