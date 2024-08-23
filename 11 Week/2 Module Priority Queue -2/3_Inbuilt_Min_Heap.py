import heapq  # this is the library which is used to use min heap


li = [1, 2, 34, 63, 3, 23, 34, 6, 23, 2, True, False, float("inf"), float("-inf")]
heapq.heapify(li)
print(li)
heapq.heappush(li, 0)
print(li)
print(heapq.heappop(li))
print(li)
# removes the minimum element add -1 then heapfiy
heapq.heapreplace(li, -1)
print(li)
