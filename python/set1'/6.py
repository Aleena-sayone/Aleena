class Circle:
    def __init__(self):  
        self.pi=3.14      
        self.getradius()
    def getradius(self,):
        self.radius=int(input("enter radius :"))
        
    def findarea(self,):
        area=self.pi*(self.radius*self.radius)
        print("area :",area)

obj=Circle()
obj.findarea()