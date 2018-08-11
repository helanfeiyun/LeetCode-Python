def twoSum(numbers, target):
    ###方法一：采用二分法查找，时间复杂度为O(nlogn)
    start, mid, end = 0, 0, len(numbers) - 1
    for i in range(len(numbers) - 1):
        start = i + 1
        end = len(numbers) - 1
        while (start <= end):
            mid = (start + end) // 2
            if numbers[mid] + numbers[i] == target:
                return [i + 1, mid + 1]
            if numbers[mid] + numbers[i] < target:
                start = mid + 1
            else:
                end = mid - 1



# def twoSum(numbers, target):
#     ###方法二：采用字典存储所需值，时间复杂度为O(n)
#     d = {}
#     for i in range(len(numbers)):
#         if target-numbers[i] in d:
#             return [d[target-numbers[i]]+1, i+1]
#         else:
#             d[numbers[i]] = i