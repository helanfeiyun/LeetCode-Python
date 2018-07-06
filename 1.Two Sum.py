# author Helanfeiyun


nums=[1,2,3,4,12,43,45,78,]
target = 88

# def sum2(nums,target):
#     for i in range(len(nums)):
#         low = i + 1
#         high = len(nums) - 1
#         while low < high:
#             mid = (low + high) // 2
#             if nums[i] + nums[mid] == target:
#                 return print([ i, mid])
#             elif nums[i] + nums[mid] < target:
#                 low = mid +1
#             else:
#                 high = mid -1
#
# sum2(nums,target)

def twoSum(nums,target):
    if len(nums) < 2:
        return 0
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict :
            return [buff_dict[nums[i]],i]
        else:
            buff_dict[target-nums[i]] = i

print(twoSum(nums,target))