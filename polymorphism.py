


##Polymorphism (Method Overloading)
class Geometry:

    def area(self,a,b=0):
        if b==0:
            print("Circle",3.14*a*a)
        else:
            print("Rect",a*b)
obj = Geometry()
obj.area(3)
obj.area(3,2)
