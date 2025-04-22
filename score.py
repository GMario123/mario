print("G Mario Shilshi Raj URK24CS1145")
score=int(input("Enter player score: "))
if 75<=score<=100:
    print("Opener")
    if 85<=score<=100: 
        print("Batsman 1")
    elif 75<=score<=84:
        print("Batsman 2")
elif 50<=score<=74:
      print("Step Down")
      if 60<=score<=74:
        print("Batsman 3")
      elif 55<=score<=59:
            print("Batsman 4")
      elif 50<=score<=54:
            print("Batsman 5")
else:
     print("More Step Down batsman")
