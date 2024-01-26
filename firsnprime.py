num=int(input("Enter the value of n:"))
i=2
k=1
while(k<=num):
flag=0
j=2 while(j<=(i/2)): if((i%j)==0):
flag=1
break
j=j+1
if(flag==0):
print(i)
16
k=k+1
i=i+1