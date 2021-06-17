m=int(input("請輸入階乘值M:"))

total=1
n=1
while(total<m):
    for i in range(1,n):
        total*=i
    n+=1
    print("n=",n)
print("超過M為",m,"的最小階乘N值為:",n)