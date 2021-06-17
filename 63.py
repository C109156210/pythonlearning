n=int(input("請輸入正整數n:"))

data=[]
i=1

while(i**2<=n):
    if n%i==0:
        data.append(i)
        data.append(n/i)
    i+=1
data.remove(n)
sum1=sum(data)

if sum1==n:
    print("perfect")
elif sum1>=n:
    print("abundant")
else:
    print("deficient")