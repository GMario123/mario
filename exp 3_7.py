print("G Mario Shilshi Raj URK24CS1145")
nums= list(map(int,input("Enter numbers separated by spaces:").split()))
freq ={}
for num in nums:
    freq[num]= freq.get(num ,0) +1
for key,value in freq.items():
    print(f"{key}:{value}")
