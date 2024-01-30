name = []
n = int(input("Enter the no of students :"))
for i in range(1, n+1):
print("Enter name", i, )
item = str(input())
name.append(item)
print(name)
name.sort()
print( "Alphabetical order",name)
