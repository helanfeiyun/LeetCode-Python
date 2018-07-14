# author Helanfeiyun

nums1=[1,3,5,7,9,0,0,0,0,0,0,0,0,0]
nums2=[]

def merge(nums1, m ,nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    if not nums2:
        return None
    while m>0 and n>0 :
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0 :
        nums1[:n] = nums2[:n]






# def merge(nums1, m, nums2, n):
#     """
#     :type nums1: List[int]
#     :type m: int
#     :type nums2: List[int]
#     :type n: int
#     :rtype: void Do not return anything, modify nums1 in-place instead.
#     """
#     if not nums2:
#         return None
#     low = 0
#     for j in range(n):
#         high = m + j -1
#         while low <= high :
#             mid = (low + high) // 2
#             if nums1[mid] == nums2[j]:
#                 for s in range(m+j-1,mid-1,-1):
#                     nums1[s+1] = nums1[s]
#                 nums1[mid] = nums2[j]
#                 low = mid
#                 break
#             elif nums1[mid] < nums2[j]:
#                 low = mid +1
#             else :
#                 high = mid -1
#         else:
#             for s in range(m+j-1,low-1,-1):
#                 nums1[s+1] = nums1[s]
#             nums1[low] = nums2[j]


merge(nums1,5,nums2,3)
print(nums1)