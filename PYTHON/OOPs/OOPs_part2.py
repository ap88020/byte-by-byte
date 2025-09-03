class Complex:
    def __init__(self, real , img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i +" , self.img,"j")

    def __add__(self , num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img

        return Complex(newReal,newImg)
        

num1 = Complex(2,5)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()
print("---------")
num3 = num1 + num2
num3.showNumber()

# c1 = Complex(3,5)
# c1.showNumber()
# c2 = Complex(3,5)
# c2.showNumber()

# class Student:
#     def __init__(self, phy,math,chem):
#         self.phy = phy
#         self.math = math
#         self.chem = chem
    
#     @property
#     def perc(self):
#         return str((self.phy + self.math + self.chem)/3) + "%"

    

# stu1 = Student(98,99,98)
# stu1.phy = 86
# stu1.math = 86
# stu1.chem = 86

# print(stu1.perc)


# class Car:
#     def __init__(self,type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("started....")

#     @staticmethod
#     def stop():
#         print("stoped....")

# class Toyota(Car):
#     def __init__(self, name,type):
#         self.name = name
#         super().__init__(type)
#         super().start()

# c1 = Toyota("Fortuner","Electric")
# print(c1.name)  
# print(c1.type)


# class A:
#     def verA():
#         print("welcome to class A")

# class B:
#     def verB():
#         print("welcome to class B")

# class C(A,B):
#     def verC():
#         print("welcome to class C")


# c1 = C

# print(c1.verA())
# print(c1.verB())
# print(c1.verC())

# class Car:
#     @staticmethod
#     def start():
#         print("start car.....")
    
#     def stop():
#         print("stopped car.....")


# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type
    
# f1 = Fortuner("diesel")

# print(f1.type)


# class TyotaCar(Car):

#     def __init__(self , name):
#         self.name = name

# c1 = TyotaCar("Fortuner")
# c2 = TyotaCar("Perus")

# print(c1.start())

# print(c1.name)
# print(c2.name)

# class Person:
#     __name = "Anonynmos"
    
#     def __hello(self):
#         print("hllo " , self.__name)

#     def welcome(self):
#         self.__hello()
    


# p1 = Person()
# print(p1.welcome())

# print(p1.__name)

# class Account:
#     def __init__(self,acc_no , acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
        
#     def resePass(self):
#         print(self.__acc_pass)

# a1 = Account(32323,"abcd")
# print(a1.acc_no)
# print(a1.resePass())

# print(a1.__acc_pass)

# class Student:
#     def __init__(self,name):
#         self.name = name


# s1 = Student("prey")

# del s1.name
# print(s1.name)



# print("hllo world")