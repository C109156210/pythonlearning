a=input("請輸入string_a:")
b=input("請輸入string_b:")

ans=[]

for i in range(0,len(a)):
    if (a[i] in b)and not(a[i] in ans):
        ans.append(a[i])

if len(ans)==0:
    print("N")
else:
    ans.sort()
    print("".join(ans))