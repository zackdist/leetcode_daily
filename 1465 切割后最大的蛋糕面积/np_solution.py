import numpy as np
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        horizontalCuts=[0]+horizontalCuts
        verticalCuts=[0]+verticalCuts

        # np.diff 返回特定轴上离散差值
        hdiff=np.max(np.diff(np.array(horizontalCuts)))
        vdiff=np.max(np.diff(np.array(verticalCuts)))
        return int(hdiff*vdiff) % (10**9 + 7)
