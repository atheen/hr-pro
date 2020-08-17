from datetime import datetime


class Employee:
   #Employee class here
   def __init__(self,name,age,salary,employment_year):
       self.name = name
       self.age = age
       self.salary = salary
       self.employment_year = employment_year
   def get_working_years(self):
       return datetime.today().year-int(self.employment_year)
   def __str__(self):
        return "Name: %s, Age: %s, Salary: %s, Working Years: %d" % (self.name, self.age, self.salary, self.get_working_years())

class Manager(Employee):
    #Manager class here
    def __init__(self,name,age,salary,employment_year,bonus_percentage):
        super().__init__(name,age,salary,employment_year)
        self.bonus_percentage = bonus_percentage
    def get_bonus(self):
        return float(self.bonus_percentage)*float(self.salary)
    def __str__(self):
         return "Name: %s, Age: %s, Salary: %s, Working Years: %d, bonus: %d" % (self.name, self.age, self.salary, self.get_working_years(),self.get_bonus())


def main():
	# main code here
    managers = []
    employees = []
    print("Welcome to HR Pro 2019")
    print("Options:")
    print("\t1. Show Employees\n\t2. Show Managers\n\t3. Add An Employee\n\t4. Add A Manager\n\t5. Exit\n")
    choice = input("What would you like to do? ")
    while choice != "5":
        print("-----------------")
        if choice == "1":
            print("Employees\n")
            for e in employees:
                print(e)
        elif choice == "2":
            print("Managers\n")
            for m in managers:
                print(m)
        elif choice == "3":
            name = input("Name: ")
            age = input("Age: ")
            salary = input("Salary: ")
            emp_year = input("Employement Year: ")
            employee = Employee(name,age,salary,emp_year)
            employees.append(employee)
            print("Employee added succesfully")
        elif choice == "4":
            name = input("Name: ")
            age = input("Age: ")
            salary = input("Salary: ")
            emp_year = input("Employement Year: ")
            bonus = input("Bonus Percentage: ")
            manager = Manager(name,age,salary,emp_year,bonus)
            managers.append(manager)
            print("Manager added succesfully")
        else:
            break
        print("-----------------\nOptions:")
        print("\t1. Show Employees\n\t2. Show Managers\n\t3. Add An Employee\n\t4. Add A Manager\n\t5. Exit\n")
        choice = input("What would you like to do? ")

if __name__ == '__main__':
	main()
