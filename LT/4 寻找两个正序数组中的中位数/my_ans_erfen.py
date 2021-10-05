class Solution:
    def findMedianSortedArrays(self, nums1, nums2 ):
        length = len(nums1)+len(nums2)
        min_list = nums1 if len(nums1)  < len(nums2) else nums2
        max_list = nums1 if len(nums1)  >= len(nums2) else nums2

        K = int(length / 2)
        start = 0
        end = len(min_list)
        while(True):
            div_1 = int((start+end)/2)
            div_2 = K - div_1 - 1

            x_i,x_i1,y_i,y_i1 = self.get_value(min_list,max_list,div_1-1,div_2)
            if (x_i > y_i1):
                end = div_1
            elif (y_i > x_i1):
                start = div_1+1
            else:
                print(x_i,x_i1)
                print(y_i,y_i1)
                if(length % 2 ==0):
                    return ( max(x_i,y_i) + min(x_i1,y_i1))/2
                else:
                    return min(x_i1,y_i1)


    def get_value(self,nums1,nums2,i,j):
        if(i<0):
            x_i = -10**6
        else:
            x_i = nums1[i]

        if( i < (len(nums1)-1)):
            x_i1 = nums1[i+1]
        else:
            x_i1 = 10**6

        if (j < 0):
            y_i = -10 ** 6
        else:
            y_i = nums2[j]

        if (j < (len(nums2) - 1)):
            y_i1 = nums2[j + 1]
        else:
            y_i1 = 10 ** 6

        return x_i,x_i1,y_i,y_i1

so = Solution()
nums1 = [2,3,4,5,6,7]
nums2 = [1]
res = so.findMedianSortedArrays(nums1,nums2)
print(res)






