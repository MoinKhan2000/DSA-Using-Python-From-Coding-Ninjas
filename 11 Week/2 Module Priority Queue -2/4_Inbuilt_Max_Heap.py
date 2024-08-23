import heapq

li = [23, 5, 2, 1, 5, 12, 24, 21, 354]
heapq._heapify_max(li)
print(li)
print(heapq._heappop_max(li))
print(li)
print(heapq._heapreplace_max(li, 444))
print(li)
# We dont have inbuilt push function for max heap
li.append(999)
# heapq._heapify_max(li)
# [999, 444, 12, 23, 5, 1, 2, 5, 21]

# alternate

heapq._siftdown_max(li, 0, len(li) - 1)
print(li)    
# [999, 444, 12, 23, 5, 1, 2, 5, 21]
# takes 3 argument 1. is list , 2nd is till where i have to swap if possible 3rd what is the current position of element which is just appended to the list


print(li)
