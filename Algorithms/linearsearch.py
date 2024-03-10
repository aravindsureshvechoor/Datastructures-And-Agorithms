def linearsearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i+1
    return None

def verify(index):
    if index is None:
        print("value not found")
    else:
        print(f"value found at {index+1}")

a=[10,20,30,40,50]
print(linearsearch(a,40))
# verify(result)

