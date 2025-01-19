thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

x = thisdict["model"]
print(x)
x1 = thisdict.get("model")
print(x1)