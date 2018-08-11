def majorityElement(nums):
    ###方法一：采用字典，key为数字，value为出现次数，时间复杂度为O(n)
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
            if d[i] > (len(nums) // 2):
                break
        else:
            d[i] = 1
    return i

# def majorityElement(nums):
#     ###方法二：转换成集合，对每个数依次使用count，时间复杂度为O(n)
#     for i in list(set(nums)):
#         if nums.count(i) > len(nums)//2  :
#             return i


# def majorityElement(nums):
#     ###方法三：一个trick,排序取中位数,时间复杂度为O(nlogn)
#     return sorted(nums)[len(nums)//2]