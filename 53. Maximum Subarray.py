# author Helanfeiyun

nums = [-2,1,2,1]


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums[0] >= 0:
        m,s = nums[0],nums[0]
    else:
        m,s = nums[0],0
    for i in range(1, len(nums)):
        if m >= 0:
            s += nums[i]
            if s < 0:
                s = 0
                continue
            if s > m:
                m = s
        else:
            if m < nums[i]:
                m = nums[i]
                s = m
    return m
print(maxSubArray(nums))


# def maxSubArray(nums):
#     '''
#
#     :param nums:
#     :return:
#     '''
#     if not nums:
#         return False
#     maxSum = curSum = nums[0]
#     for i in nums[1:]:
#         curSum = max(i,curSum+i)
#         maxSum = max(maxSum,curSum)
#     return maxSum