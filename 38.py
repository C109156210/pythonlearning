n=int(input("n="))
for i in range(-int(n/2),int(n/2)+1):
  print(" "*abs(i),"*"*abs(n-abs(i)*2))