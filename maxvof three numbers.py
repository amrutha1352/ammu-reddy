 In [73]:
x=int(input("enter first num"))
y=int(input("enter second num"))
z=int(input("enter third num"))
if x>y:
  if x>z:
    print("the max num of the three num",x)
  else:
    print("the max num of the three num",z)
else:
  if y>z:
   print("the max num of the three num",y)
  else:
   print("the max num of the three num",z)