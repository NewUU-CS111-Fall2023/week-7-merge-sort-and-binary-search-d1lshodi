def missingNumber(nums):
    # Runtime Complexity: O(n)
    expected_sum = len(nums) * (len(nums) + 1) // 2
    actual_sum = sum(nums)
    missing_number = expected_sum - actual_sum
    
    return missing_number