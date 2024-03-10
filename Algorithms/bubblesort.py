x=[1,2,3,4,5,6,7,8,9,10,5,5,5,5]
for i in range(len(x)):
    for j in range(i,len(x)):
        if x[i]>x[j]:
            temp=x[i]
            x[i]=x[j]
            x[j]=temp
print(x)


