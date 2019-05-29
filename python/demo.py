# p2.py
class P:
   def __init__(self, name, alias):
      self.name = name       # public
      self.__alias = alias   # private

   def who(self):
      print('name  : ', self.name)
      print('alias : ', self.__alias)

   def __foo(self):          # private method
      print('This is private method')

   def foo(self):            # public method
      print('This is public method')
      self.__foo()


x = P('Alex', 'amem')
x.foo()
x.who()
x._P__foo()

class Myclass:
    def __init__(self,fname,lname):
        self.fname=fname
        self.__lname=lname
    def who(self):
        print("fname :", self.fname)
        print("lname  : ", self.__lname)
    def __foo(self):
        print("private variable : lname => ",self.__lname)

y=Myclass('ajumon','thomas')
y.who()
y._Myclass__foo()