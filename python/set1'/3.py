class Myclass:
    def __init__(self,):
        self.getstring()
    def getstring(self):
        self.string1=input("enter your string here : ")
    def putstring(self):
        print("You have typed : ",self.string1.upper())

obj=Myclass()
obj.putstring()