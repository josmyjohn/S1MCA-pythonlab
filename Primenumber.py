upper=int(input("enter the upper limit:"))
lower=int(input("enter the lower limit:"))
print("prime no between",lower,"and",upper,"are:")
for i in range(lower,(upper+1)):
f=0
j=2
while(j<=(i/2)):
if((i%j)==0):
f=1
break
j=j+1
if(f==0):
print(i)
