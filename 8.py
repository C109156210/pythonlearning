x=input("輸入第一行正整數為:")
a=input("第二行中數列中的數字為:").split(" ")
list1=[]
for j in range(0,int(x)):
    c=a.count(a[j])
    list1.append(c)
if max(list1)==1:
    print("每個數字剛好出現一次")
else:
    b=max(list1)
    print("最大出現次數的數字為:"+str(a[list1.index(b)]))
    print("出現次數:"+str(b))