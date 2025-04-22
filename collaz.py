num = int(input("Enter a number: "))
steps = 0
sequence = [] 
while num != 1:
    sequence.append(num)
    if num % 2 == 0:
        num = num // 2
    else:
     num=num *3+1
    steps +=1
sequence.append(1)
print("collatz sequence:",sequence)
print("Total steps:",steps)
print("G Mario Shilshi Raj URK24CS1145")
