def insertion_sort(arr):
    for i in range(1, len(arr)):
        current=arr[i]
        pos=i
        while current<arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos-=1
        arr[pos]=current

# Example usage
array = [9, 5, 1, 4, 3]
insertion_sort(array)
print("Sorted array:", array)


