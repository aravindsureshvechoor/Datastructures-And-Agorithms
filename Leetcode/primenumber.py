def prime(arr):
    x = []
    for i in range(len(arr)):
        prime = True
        for j in range(2, i):
            if arr[i] % j == 0:
                prime = False
                break
        if prime:
            x.append(arr[i])
    return x



arr = [1,3,5,7,8]

print(prime(arr))




