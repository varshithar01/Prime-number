n=10
flag=True
l=[]
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
        else:
            flag=True
    if flag:
        l.append(i)

for num in l:
    print(num)
    