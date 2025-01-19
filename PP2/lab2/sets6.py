x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)
############
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
############
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set4 = set1 & set2
print(set4)

set1.intersection_update(set2)
print(set1)