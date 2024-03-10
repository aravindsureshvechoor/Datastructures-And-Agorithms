def second_largest(arr):
    largest = float('-inf')
    secondlargest = float('-inf')

    for i in range(len(arr)):
        if arr[i] > largest:
            secondlargest = largest
            largest = arr[i]
        elif arr[i] > secondlargest:
            secondlargest = arr[i]

    return secondlargest

arr = [1, 3, 400, 5, 7]
result = second_largest(arr)
print(result)
