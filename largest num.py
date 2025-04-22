numbers=[]
print("G Mario Shilshi Raj URK24CS1145")
print("Enter 10 Numbers") 
for i in range(10):
    num=int(input(f"number{i+1}: "))
    numbers.append(num)

maximum= max(numbers)
print("Maximum Number: ",maximum)


