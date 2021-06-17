km=float(input("請輸入路程公里數(km):"))


if km>1.5:
    if km%0.25>0:
        a=(km-1.5)//0.25+1
        print("所需車資為:",int(75+a*5))
    else:
        a=(km-1.5)//0.25
        print("所需車資為:",int(75+a*5))
else:
    print("所需車資為:",75)