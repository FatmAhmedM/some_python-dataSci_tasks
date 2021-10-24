class hand:
    def __init__ (self, handd):
        self.hand =handd

    def calchand (self):
        return (self.hand*2)


class legandhand:
    def __init__(self, hand1, leg):
        self.hand1 = hand1
        self.leg = leg
        self.handleg = hand(self.hand1)

    def calchl (self):
        return "hands and legs:" + str(self.handleg.calchand() + self.leg)


obj = legandhand(1,2)
print(obj.calchl())


class Salary:
    def __init__(self, pay):
        self.pay = pay
 
    def get_total(self):
        return (self.pay*12)
 
 

 """"
class Employee:
    def __init__(self, pay1, bonus):
        self.pay1 = pay1
        self.bonus = bonus
        self.obj_salary = Salary(self.pay1)
 
    def annual_salary(self):
        return "Total: " + str(self.obj_salary.get_total() + self.bonus)
 
 
obj_emp = Employee(600, 500)
print(obj_emp.annual_salary())
"""


        