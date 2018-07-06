# author Helanfeiyun

nums=[1,2,3,3,4,5,5,5,7,7,7]

# def removeDuplicates(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if len(nums) < 1:
#         return False
#     for i in range(len(nums) - 1):
#         while True:
#             if i+1 < len(nums):
#                 if nums[i + 1] == nums[i]:
#                     del nums[i + 1]
#                 else:
#                     break
#             else:
#                 break
#         print(len(nums)-1)
#     return len(nums)


def removeDuplicates(A):
    if not A:
        return 0

    newTail = 0

    for i in range(1, len(A)):
        if A[i] != A[newTail]:
            newTail += 1
            A[newTail] = A[i]

    return newTail + 1

length = removeDuplicates(nums)
print(length)



