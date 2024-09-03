def leftBinarySearch(needle, nums):
    low = 0
    high = len(nums) - 1

    while low + 1 < high:
        median = int((low + high) / 2)
        if nums[median] < needle:
            low = median
        else:
            high = median
        print(nums, f'low is: {low}', f'high is: {high}')

    if nums[low] == needle:
        return low
    if nums[high] == needle:
        return high
    return -1


leftBinarySearch(1, [1, 2, 3, 3, 3, 5, 6, 7, 10, 11, 14])
