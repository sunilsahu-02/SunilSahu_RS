T=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
L=[]
for i in T:
    s=0
    for j in i:
        s=s+j
    avg=s/len(i)
    L.append(avg)
print(L)