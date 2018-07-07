# author Helanfeiyun

nums = [1,3,5,6]
target = 2

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums:
        return 0
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    else:
        if target > nums[low]:
            return low+1
        return low

print(searchInsert(nums,target))


# def searchInsert(self, nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#     return len([x for x in nums if x < target])