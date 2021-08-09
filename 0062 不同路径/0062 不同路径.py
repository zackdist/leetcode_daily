# 28ms	15.2MB
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 输入长度m 宽度n
        # 记录从左上到达右下具有不同走法
        # 只能向下走或者向右走
        # dp（i,j）= dp(i-1,j)+dp(i,j-1)
        # dp (i,0) = i
        # dp (0,j) = j

        # 初始化
        dp_m = [[0] * n for i in range(m)]
        for i in range(n):
            dp_m[0][i] = 1
        for j in range(m):
            dp_m[j][0] = 1

        def get_res(i,j):
            if(i==0 or j==0):
                return dp_m[i][j]
            elif(dp_m[i][j]!=0):
                return dp_m[i][j]
            else:
                dp_m[i][j] = get_res(i-1,j)+get_res(i,j-1)
                return dp_m[i][j]

        get_res(m-1,n-1)
        return dp_m[m-1][n-1]

so = Solution()
res = so.uniquePaths(23,12)
print(res)