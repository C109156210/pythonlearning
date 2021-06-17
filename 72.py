n=int(input("請輸入n:"))
k=int(input("請輸入k:"))

ans=n

while(n//k!=0):
    new=n//k
    ans+=new
    n=n%k+new
print("Peter可以抽%d支紙菸"%(ans))