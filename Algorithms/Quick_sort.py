def quicksort(arr):
    if len(arr)<=1:
        return  arr
    pivot=arr[len(arr)//2]
    smaller=[x for x in arr if x<pivot]
    equal=[x for x in arr if x==pivot]
    larger=[x for x in arr if x>pivot]

    return quicksort(smaller) + equal + quicksort(larger)
arr=[9,8,6,5,1,2]
print(quicksort(arr))
