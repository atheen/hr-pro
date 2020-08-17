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

class Manager(Employee):
    #Manager class here
    def __init__(self,name,age,salary,employment_year,bonus_percentage):
        Employee.__init__(self,name,age,salary,employment_year)
        self.bonus_percentage = bonus_percentage
    def get_bonus(self):
        return float(self.bonus_percentage)*float(self.salary)

def main():
	# main code here
    managers = [Manager("sammy",52,4600,2005,.5)]
    employees = [Employee("Ahmed",40,1500,2010)]
    print("Welcome to HR Pro 2019")
    print("Options:")
    print("\t1. Show Employees\n\t2. Show Managers\n\t3. Add An Employee\n\t4. Add A Manager\n\t5. Exit\n")
    choice = input("What would you like to do? ")
    while choice != "5":
        print("-----------------")
        if choice == "1":
            print("Employees\n")
            for e in employees:
                print("Name: %s, Age: %s, Salary: %s, Working Years: %s"%(e.name,e.age,e.salary,e.get_working_years()))
        if choice == "2":
            print("Managers\n")
            for m in managers:
                print("Name: %s, Age: %s, Salary: %s, Working Years: %s, Bonus: %.6f"%(m.name,m.age,m.salary,m.get_working_years(),m.get_bonus()))
        if choice == "3":
            name = input("Name: ")
            age = input("Age: ")
            salary = input("Salary: ")
            emp_year = input("Employement Year: ")
            employee = Employee(name,age,salary,emp_year)
            employees.append(employee)
            print("Employee added succesfully")
        if choice == "4":
            name = input("Name: ")
            age = input("Age: ")
            salary = input("Salary: ")
            emp_year = input("Employement Year: ")
            bonus = input("Bonus Percentage: ")
            manager = Manager(name,age,salary,emp_year,bonus)
            managers.append(manager)
            print("Manager added succesfully")
        print("-----------------\nOptions:")
        print("\t1. Show Employees\n\t2. Show Managers\n\t3. Add An Employee\n\t4. Add A Manager\n\t5. Exit\n")
        choice = input("What would you like to do? ")

if __name__ == '__main__':
	main()
