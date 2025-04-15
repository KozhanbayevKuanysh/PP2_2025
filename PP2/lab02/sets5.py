thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
############
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set4 = set1 | set2
print(set4)
#########
myset1 = {"a", "b", "c"}
myset2 = {1, 2, 3}
myset3 = {"John", "Elena"}
myset4 = {"apple", "bananas", "cherry"}
myset5 = myset1.union(myset2, myset3, myset4)
print(myset5)
myset6 = myset1 | myset2 | myset3 |myset4
print(myset6)