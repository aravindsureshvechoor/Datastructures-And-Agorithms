def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low <= high:
        midpoint=(low+high)//2
        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            low = midpoint+1
        else:
            high = midpoint-1
    return None
def verify(result):
    if result is None:
        print("target not found")
    else:
        print(f"target found at {result+1}")










a=[10,20,30,40,50]
b=binary_search(a,40)
verify(b)

