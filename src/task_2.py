def max_beautifulness(n, permutation):
    # Runtime Complexity: O(n)

    initial_beautifulness = sum(abs(permutation[i] - (i + 1)) for i in range(n))
    max_beautifulness = initial_beautifulness

    for i in range(n):
        swapped_permutation = permutation.copy()
        swapped_permutation[i], swapped_permutation[permutation[i] - 1] = swapped_permutation[permutation[i] - 1], swapped_permutation[i]
        current_beautifulness = sum(abs(swapped_permutation[j] - j - 1) for j in range(n))
        max_beautifulness = max(max_beautifulness, current_beautifulness)

    return max_beautifulness