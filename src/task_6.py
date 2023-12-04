def search_insert(nums, target):
    # Runtime Complexity: O(log(n))

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return 1, mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, low