print("Rectangle")
print(".........")
l=int(input("Enter length of rectangle ")) b=int(input("Enter breadth of rectangle ")) area=lambda l1,b1:l1*b1
print("Area of rectangle is ",area(l,b))
per=lambda l,b:2*(l+b)
print("Perimeter of rectangle is ",per(l,b)) print("Square")
52
print(".........")
a=int(input("Enter length of one side of square "))
area=lambda a:a*a
print(" Area of square is ",area(a))
per=lambda a:4*a
print("Perimeter of square is ",per(a))