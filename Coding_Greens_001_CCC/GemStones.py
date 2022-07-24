def gemstones(arr):
    return len(set.intersection(*arr))    # find the common elements and its maximum
n = int(input())   # input
arr = []
for i in range(n):
    arr_item = set(input())   #input array
    arr.append(arr_item)   # append the array items in the created arr
print(gemstones(arr))
    