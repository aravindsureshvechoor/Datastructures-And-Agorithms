x=[3,4,2,2,6,10,10,1]
for i in range(len(x)):
    min_val=min(x[i:])
    min_ind=x.index(min_val,i)
    temp=x[i]
    x[i]=min_val
    x[min_ind]=temp
print(x)
