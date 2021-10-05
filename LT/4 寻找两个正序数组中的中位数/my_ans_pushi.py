class Solution:
    def findMedianSortedArrays(self, nums1, nums2 ):
        num = 0
        min_1,min_2 = 0,0

        length = len(nums1) + len(nums2)
        while(num< (length/2+1)):
            left = nums1[0] if(len(nums1) > 0) else 10**6
            right = nums2[0] if(len(nums2) > 0) else 10**6

            if(left < right):
                min_x = left
                if (len(nums1) > 0):
                    nums1.pop(0)

            else:
                min_x = right
                if(len(nums2)>0):
                    nums2.pop(0)

            min_1 = min_2
            min_2 = min_x
            num = num + 1

        if(length % 2 !=0):
            print("奇数")
            return min_1
        else:
            print("偶数")
            return (min_1+min_2)/2


so = Solution()
nums1 = []
nums2 = [1]
res = so.findMedianSortedArrays(nums1,nums2)
print(res)