''' write a python program which will adding items total of prices inputed by 
the user. the adding stops as soon as user presses q from the keyboard.'''


sum = 0
while(True):
    userinput = (input("Enter the price/ or  press to 'q' to quit: \n "))
    if (userinput!= 'q'):
      sum = sum + int(userinput)
      print(f"Order  total so far: {sum}")
    elif(userinput == '-'):
      minus = sum-userinput
      print(f"Order total so far: {sum}")
    else:
      print(f"Your total bill is {sum}/-. thanks! for shopping with us.")
      break