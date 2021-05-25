class Solution:
    def get(self,stack, remain, res):
        if (len(remain) == 0):
            res.append(stack.copy())
            return res
        remain_copy = remain.copy()
        for i in remain:
            stack.append(i)
            remain_copy.remove(i)
            res = self.get(stack, remain_copy, res)
            stack.remove(i)
            remain_copy.append(i)
        return res
    def permute(self, nums):
        return self.get([], nums, [])


