import math

# 32ms  14.8MB  慢了 因为进行了多余的计算，有很多是重复计算 n！的多余计算量
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 直接利用数学公式计算
        # 即一共从 m+n 的空位中，选取n个作为向右的路径
        # 即结果为  C_(m+n-2)^n
        res = int(math.factorial(n+m-2)/(math.factorial(n-1)*math.factorial(m-1)))
        return res


so = Solution()
res = so.uniquePaths(3,7)
print(res)