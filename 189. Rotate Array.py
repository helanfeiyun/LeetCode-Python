def rotate(nums, k):
    ###用取余法去掉循环，将数组分为两段，然后两段重排，时间复杂度为O(n)
    if k == 0:
        return None
    l = len(nums)
    k = k % l
    nums[:] = nums[l-k:] +nums[:l-k]
