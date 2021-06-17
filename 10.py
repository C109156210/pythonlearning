import numpy as np

n,m=input("請輸入N,M為:").split(" ")


array1=[]
for stri in range(int(n)):
   array1.append([int(m) for m in input("輸入矩陣數值第"+str(stri+1) +"列為:").split()])
ab=np.transpose(array1).tolist()

print(type(ab[0][0]))

for j in range(int(m)):
  print("輸出矩陣數值第"+str(j+1)+"列為:",end="")
  for q in range(int(n)):
    print(str(ab[j][q])+" ",end="")
  print()