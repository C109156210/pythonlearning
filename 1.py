number=input("請輸入正整數:")
a=[]
b=[]
c=[]
d=[]

for i in range(len(number)):
    for j in range(len(number)):
        a.append(number[i:j+1])

for x in range(len(a)):
    if a[x]=='':
        continue
    else:
        b.append(a[x])
for z in b:
    if int(z)>1:
        for y in range(2,int(z)):
            if int(z)%y==0:
                break
        else:
            c.append(z)

c.sort()
if len(c)>0:
    print("子字串中最大的質數值為:",c[-1:])
else:
    print("子字串中最大的質數值為:No prime found")
