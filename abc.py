bullVariable1 = True
stringVariable1 = "Hello"
stringVariable2 = "World"
stringVariable3 = "YeonSeo"
space = " "
while(bullVariable1):
  x = input("Enter a number.")
  if (x == "1"):
    print(stringVariable1 + space + stringVariable2)
  elif (x == "2"):
    print(stringVariable1 + space + stringVariable3)
  elif (x == "3"):
    print(stringVariable3 + space + stringVariable1)
  elif (x == "4"):
    print(stringVariable2 + space + stringVariable1)
  elif (x == "5"):
    print(stringVariable3 + space + stringVariable2)
  elif (x == "6"):
    bullVariable1 = False 
  else: 
    print("option is not available") 
