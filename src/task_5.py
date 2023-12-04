from collections import Counter
import heapq

def top_k_frequent(nums, k):

    freq_counter = Counter(nums)
    heap = []
    for num, freq in freq_counter.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    result = [item[1] for item in heap]
    result.reverse()  

    return result