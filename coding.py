mathVar1 = 3
mathVar2 = 4
loopVar = True
menu = "1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Floor\n7. quit\nEnter a number\n"


while(loopVar):
  x = input(menu)
  if (x == "1"):
    print(mathVar1 + mathVar2)
  elif (x == "2"):
    print (mathVar1 - mathVar2)
  elif (x == "3"):
    print (mathVar1 * mathVar2)
  elif (x == "4"):
    print (mathVar1 / mathVar2)
  elif (x == "5"):
    print (mathVar1 % mathVar2)
  elif (x == "6"):
    print (mathVar1 // mathVar2)
  elif (x == "7"):
    loopVar = False
  else:
    print ("Not an option")
