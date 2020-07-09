input1 = input("Enter the first input: ")
input2 = input("Enter the second input: ")
input3 = input("Enter the third input: ")
if input1==input2 and input2==input3:
  print("The given inputs are equal.")
else:
  if input1==input2 or input2==input3 or input3==input1:
    print("Two inputs are equal.")
  else:
    print("None of the inputs are equal.")