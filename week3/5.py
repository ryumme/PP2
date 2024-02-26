class meth:
    def getString(self):
        self.string = input()
    
    def printString(self):
        print(self.string.upper())

x = meth()
x.getString()
x.printString()
