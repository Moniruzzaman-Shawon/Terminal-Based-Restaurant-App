# Customer
# Employee
# Admin

from abc import ABC  # abc module stands for Abstract Base Classes
# abc inherits from ABC, it becomes an abstract class

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone 
        self.email = email 
        self.address = address
      
class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

# emp = Employee("Rahim", 555, 'rahim@gmail.com', 'Dhaka', 23, 'Chef', 12000)
# print(emp.name)

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    
    
    def add_employee(self,name,email,phone,address,age, designation, salary):
        employee = Employee(name,email,phone,address,age, designation, salary) # an object will be created in Employee class
        self.employees.append(employee) # append() is used to add an item to the end of a list
        print (f'{name} is added in the list')

    def view_employee(self):
        print("---Employee List---")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)
        

class Restaurant:
    def __init__(self, name):
        self.name = name  
        self.employees = [] # work as database

    def add_employee(self,employee):
        self.employees.append(employee) # append() is used to add an item to the end of a list


ad = Admin('Karim', '1233454', 'karim@gmail.com', 'Dhaka')
ad.add_employee('Sagor', 'sagor@gmail.com', '1235123', 'Khulna', 32 , 'Chef', 34000)

ad.view_employee()
        