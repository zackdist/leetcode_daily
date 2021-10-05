# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # 获取 exponent 浮点类型
        if(exponent == 0 ):
            return 1
        if(exponent == 1 ):
            return base

        expo = exponent if exponent >0 else -exponent
        res = 1

        while(expo & 0xffffffff != 0):
            if(expo & 1 !=0):
                res = res * base
            expo = expo >> 1
            base = base * base

        return res if exponent >0 else 1/res

so = Solution()
res = so.Power(2,-1)
print(res)