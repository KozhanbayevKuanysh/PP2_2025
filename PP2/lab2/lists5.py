thislist1 = ["apple", "banana", "cherry"]
thislist1[1] = "blackcurrant"
print(thislist1)

thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist2[1:3] = ["blackcurrant", "watermelon"]
print(thislist2)

thislist3 = ["apple", "banana", "cherry"]
thislist3[1:2] = ["blackcurrant", "watermelon"]
print(thislist3)

thislist4 = ["apple", "banana", "cherry"]
thislist4[1:3] = ["watermelon"]
print(thislist4)

thislist5 = ["apple", "banana", "cherry"]
thislist5.insert(2, "watermelon")
print(thislist5)