number=input("輸入一組四位數字為:")
list1=list(map(int,number))

for i in range(len(list1)):
    a=((list1[0]+7)%10)
    b=((list1[1]+7)%10)
    c=((list1[2]+7)%10)
    d=((list1[3]+7)%10)
print("%d%d%d%d"%(c,d,a,b))