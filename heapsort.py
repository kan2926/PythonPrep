import heapq
heap = [23, 7, -4, 18, 23, 42, 37, 2, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(heap)
print(heapq.nlargest(3, heap))  # [42, 42, 37]
print(heapq.nsmallest(3, heap))
heapq._heapify_max(heap)
print(heapq._heappop_max(maxheap))
