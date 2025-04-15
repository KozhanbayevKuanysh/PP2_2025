class GetString:
    def getstring(self):
        self.text = input("Enter a string: ")
    def printstring(self):
        print(self.text.upper())

str_obj = GetString()
str_obj.getstring()
str_obj.printstring()