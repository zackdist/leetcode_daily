class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # 设定几个边界条件
        memo = {}
        def search(k,n):
            if((k,n) in memo):
                return  memo[k, n]
            if(n==0):
                return 0
            if(k<=1):
                return n

            left,right = 1,n
            # 二值逼近
            while(left + 1 < right):
                x = left + right // 2
                left_se = search(k-1,x-1)
                right_se = search(k,n-x)

                if(left_se < right_se):
                    left = x
                elif(left_se > right_se):
                    right = x
                else:
                    left = right = x

            ans = 1 + min(max(search(k - 1, x - 1), search(k, n - x))
                          for x in (left, right))
            memo[k, n] = ans

            return memo[k, n]

        res = search(k, n)
        # ans = search(k, n)
        return res

solution = Solution()
res = solution.superEggDrop(2,7)
print(res)