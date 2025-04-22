print("G Mario Shilshi Raj URK24CS1145")
a= float(input("Enter the first side of the triangle: "))
b= float(input("Enter the second side of the triangle: "))
c= float(input("Enter the third side of the triangle: "))
if a+b<=c or b+c<=a or a+c<=b:
     print("Not a Triangle")
elif a==b==c:
     print("Equilateral")
elif a==b or b==c or c==a:
     print("Isosceles")
else:
     print("Scalene")
