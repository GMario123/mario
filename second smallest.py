print("G Mario Shilshi Raj URK24CS1145")
nums = sorted(set(map(int,input("Enter numbers:").split())),reverse=True)
if len(nums)>1:
     print("The second largest number is:",nums[1])
else:
     print("No second largest number found.")
