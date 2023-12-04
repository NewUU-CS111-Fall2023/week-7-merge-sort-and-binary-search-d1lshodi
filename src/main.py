
# Author:MUXTOROV DILSHOD
# Date:4.12.2023
# Name:

from task_1 import remaining_sum_after_operations
from task_2 import max_beautifulness
from task_4 import kth_smallest
from task_5 import top_k_frequent
from task_6 import search_insert
from task_7 import recursivePow
from task_8 import missingNumber
from task_9 import findKthPositive
from task_10 import kthFactor

print("TASK 1")
T = 2
test_cases = [
    {"N": 4, "A": [2, 5, 3, 2]},
    {"N": 4, "A": [1, 1, 1, 1]}
]

output = remaining_sum_after_operations(T, test_cases)
print(output)

print("TASK 2")
n = 5
permutation = [1, 4, 2, 3, 5]

result = max_beautifulness(n, permutation)
print(result)




print("TASK 4")
n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(kth_smallest(matrix, k))

print("TASK 5")
# The runtime complexity of this solution is O(n + k * log(k)), 
# where n is the size of the input array nums. 
# The Counter operation takes O(n) time, 
# and the heap operations take O(k * log(k)) time.

size = int(input())
nums = list(map(int, input().split()))
k = int(input())

output = top_k_frequent(nums, k)
print(*output)

print("TASK 6")
size = int(input())
nums = list(map(int, input().split()))
target = int(input())

result_type, result_index = search_insert(nums, target)

print(result_type, result_index)


print("TASK 7")

x = 2
n = 4

result = recursivePow(x, n)
print(result)

print("TASK 8")
n = int(input())
nums = list(map(int, input().split()))

result = missingNumber(nums)
print(result)


print("TASK 9")

n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = findKthPositive(arr, k)
print(result)

print("TASK 10")

n, k = map(int, input().split())

result = kthFactor(n, k)
print(result)
