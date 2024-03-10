def primenumbers():
    count = 0
    sum = 0
    for i in range(2, 101):
        prime = True
        for j in range(2, i//2 + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            count += 1
            sum += i
    avg = sum/ count

    print(avg)

primenumbers()
