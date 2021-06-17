fee=input("輸入月租費型式及通話時間為:").split(",")
a=int(fee[0])
b=int(fee[1])
if a==186:
    if b*0.09*2>a:
        print("通話費為:"+str(int(round(b*0.09*0.8,0))))
    elif b*0.09*2<=a:
        print("通話費為:"+str(int(round(b*0.09*0.9,0))))
elif a==386:
    if b*0.08*2>a:
        print("通話費為:"+str(int(round(b*0.08*0.7,0))))
    elif b*0.08*2<=a:
        print("通話費為:"+str(int(round(b*0.08*0.8,0))))
elif a==586:
    if b*0.07*2>a:
        print("通話費為:"+str(int(round(b*0.07*0.6,0))))
    elif b*0.07*2<=a:
        print("通話費為:"+str(int(round(b*0.07*0.7,0))))
elif a==986:
    if b*0.06*2>a:
        print("通話費為:"+str(int(round(b*0.06*0.5,0))))
    elif b*0.07*2<=a:
        print("通話費為:"+str(int(round(b*0.06*0.6,0))))
else:
    print("沒有這個月租費型式")