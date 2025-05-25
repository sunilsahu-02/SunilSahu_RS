n = int(input("Enter a natural number: "))
for i in range(1,n+1):
    sum=0
    for j in range(1,i+1):
        sum=sum + j**2
    print(sum)
