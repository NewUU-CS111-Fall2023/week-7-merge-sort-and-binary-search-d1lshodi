def remaining_sum_after_operations(T, test_cases):
    # Runtime Complexity: O(T * N * log(N))
    # T is the number of test cases, N is the number of elements in the array

    results = []

    for t in range(T):
        N = test_cases[t]["N"]
        A = test_cases[t]["A"]
        remaining_sum = 0
        for length in range(3, N + 1, 2):
            medians = []
            for i in range(N - length + 1):
                subarray = A[i:i + length]
                subarray.sort()
                median = subarray[length // 2]
                medians.append(median)
            min_median = min(medians)
            A.remove(min_median)
            remaining_sum += sum(A)

        results.append(remaining_sum)

    return results