class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = nums1
        lst.extend(nums2)
        lst = sorted(list(lst))
        # print(lst)
        if len(lst)%2==0:
            median = (lst[(len(lst)//2)] + lst[(len(lst)//2)-1]) / 2
        else:
            median = lst[(len(lst)//2)]
        return median