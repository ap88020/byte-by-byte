class Account:
    def __init__(self,balance,account):
        self.balance = balance
        self.account = account
    
    def debit(self, dbt):
        self.balance -= dbt 
        print("you debit " , dbt , " rupees from this account no :" , self.account , " now your current balace is " , self.balance)
    
    def credit(self, credit):
        self.balance += credit 
        print("you credit " , credit , " rupees from this account no :" , self.account , " now your current balace is " , self.balance)


a1 = Account(40,"asdkj8987878")
# a1.debit(20)
a1.credit(30)


# class Car:
#     def __init__(self):
#         self.acc = False
#         self.clutch = False
#         self.brk = False
    
#     def srt(self):
#         self.clutch = True
#         self.acc = True
#         self.brk = True

#         print("car started..")


# c1 = Car()
# c1.srt()


# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     @staticmethod
#     def college():
#         print("hllo world")

#     def get_val(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi ", self.name , " your avg marks is :" , sum / 3)


# s1 = Student("tony staks", [99,98,97])
# s1.get_val()
# s1.college()

# class Student:
    
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student on database..")

#     def greet(self):
#         print("welcome to mine new world")
    
#     def get_marks(self):
#         return self.marks


# s1 = Student("ap",77)
# s1.greet()
# print(s1.get_marks())

# s1 = Student("ap",98)
# print(s1.name , s1.marks)
# s2 = Student("ap_ap",77)
# print(s1.name,s2.marks)

# class Car:
#     color = "Black"
#     model = "BMW"


# c1 = Car()
# print(c1.color)
# print(c1.model)

# class Student :
#     name = "akash"


# s1 = Student()

# print(s1.name)