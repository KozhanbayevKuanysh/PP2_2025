def myfunc(n):
  return abs(n - 50)

thislist1 = [100, 50, 65, 82, 23]
thislist1.sort(key = myfunc)
print(thislist1)

thislist2 = ["banana", "Orange", "Kiwi", "cherry"]
thislist2.sort(key = str.lower)
print(thislist2)

thislist3 = ["banana", "Orange", "Kiwi", "cherry"]
thislist3.reverse()
print(thislist3)