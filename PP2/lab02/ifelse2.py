a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
elif a > b or a > c:
  print("At least one of the conditions is True")
elif not a > b:
  print("a is NOT greater than b")
##############
x = 34
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
###########
a = 33
b = 200
if b > a:
  pass # put in the pass statement to avoid getting an error.