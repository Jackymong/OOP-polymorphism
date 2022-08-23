#Polymorphism ( Method Overriding )
class Phone:
    def __init__(self,price,brand,cemera):
        print("Inside phone constructor")
        self.__price = price
        self.__brand = brand
        self.__camera = cemera

    def buy(self):
        print("Buying phone")

    def return_phone(self):
        print("Return phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def buy(self):
        print("Buying a Smartphone")

s = SmartPhone(12000,"Apple",13)
s.buy()


#Polymorphism (Method Overloading)
class Geometry:

    def area(self,a,b=0):
        if b==0:
            print("Circle",3.14*a*a)
        else:
            print("Rect",a*b)
obj = Geometry()
obj.area(3)
obj.area(3,2)  
