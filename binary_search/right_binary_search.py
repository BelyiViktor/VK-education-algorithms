def rightBinarySearch(needle, nums):
    low = 0
    high = len(nums) - 1
    while low + 1 < high:
        median = int((low + high) / 2)
        if nums[median] <= needle:
            low = median
        else:
            high = median
        if nums[high] == needle:
            return high
        if nums[low] == needle:
            return low
    return -1


print(rightBinarySearch(5, [1, 2, 3, 4, 5, 6]))
