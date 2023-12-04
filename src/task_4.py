def count_less_equal(matrix, target):
    n = len(matrix)
    count = 0
    i, j = n - 1, 0

    # Runtime Complexity: O(n)
    while i >= 0 and j < n:
        if matrix[i][j] <= target:
            count += (i + 1) 
            j += 1
        else:
            i -= 1

    return count

def kth_smallest(matrix, k):
    n = len(matrix)
    
    # Runtime Complexity: O(n * log(range))
    low, high = matrix[0][0], matrix[n - 1][n - 1]

    while low < high:
        mid = low + (high - low) // 2
        count = count_less_equal(matrix, mid)

        if count < k:
            low = mid + 1
        else:
            high = mid

    return low