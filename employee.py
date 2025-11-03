# Using Dictionary

employees = []

def add():
    emp_id = int(input("ID: "))
    name = input("Name: ")
    job = input("Job: ")
    salary = int(input("Salary: "))
    employees.append({"id": emp_id, "name": name, "job": job, "salary": salary})
    print("Added!")

def update():
    emp_id = int(input("ID to Update: "))
    for e in employees:
        if e["id"] == emp_id:
            e["salary"] = int(input("New Salary: "))
            print("Updated!")
            return
    print("Not Found!")

def delete():
    emp_id = int(input("ID to Delete: "))
    for e in employees:
        if e["id"] == emp_id:
            employees.remove(e)
            print("Deleted!")
            return
    print("Not Found!")

def show():
    for e in employees:
        print(e)

while True:
    print("\n1.Add  2.Update  3.Delete  4.Show  5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1: add()
    elif ch == 2: update()
    elif ch == 3: delete()
    elif ch == 4: show()
    elif ch == 5: break
    else: print("Invalid!")


# Using Object (Class)

class Employee:
    def __init__(self, emp_id, name, job, salary):
        self.id, self.name, self.job, self.salary = emp_id, name, job, salary

class Manager:
    employees = []

    @classmethod
    def add(cls):
        emp = Employee(int(input("ID: ")), input("Name: "), input("Job: "), int(input("Salary: ")))
        cls.employees.append(emp); print("Added!")

    @classmethod
    def update(cls):
        emp_id = int(input("ID to Update: "))
        for e in cls.employees:
            if e.id == emp_id:
                e.salary = int(input("New Salary: "))
                print("Updated!"); return
        print("Not Found!")

    @classmethod
    def delete(cls):
        emp_id = int(input("ID to Delete: "))
        for e in cls.employees:
            if e.id == emp_id:
                cls.employees.remove(e); print("Deleted!"); return
        print("Not Found!")

    @classmethod
    def show(cls):
        for e in cls.employees:
            print(e.id, e.name, e.job, e.salary)

while True:
    print("\n1.Add  2.Update  3.Delete  4.Show  5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1: Manager.add()
    elif ch == 2: Manager.update()
    elif ch == 3: Manager.delete()
    elif ch == 4: Manager.show()
    elif ch == 5: break
    else: print("Invalid!")



# Using List

employees = []

def add(): employees.append([int(input("ID: ")), input("Name: "), input("Job: "), int(input("Salary: "))])
def update():
    emp_id = int(input("ID to Update: "))
    for e in employees:
        if e[0] == emp_id:
            e[3] = int(input("New Salary: ")); print("Updated!"); return
    print("Not Found!")
def delete():
    emp_id = int(input("ID to Delete: "))
    for e in employees:
        if e[0] == emp_id:
            employees.remove(e); print("Deleted!"); return
    print("Not Found!")
def show(): [print(e) for e in employees]

while True:
    print("\n1.Add  2.Update  3.Delete  4.Show  5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1: add()
    elif ch == 2: update()
    elif ch == 3: delete()
    elif ch == 4: show()
    elif ch == 5: break
    else: print("Invalid!")



# Using Tuple

eemployees = []

def add():
    emp = (int(input("ID: ")), input("Name: "), input("Job: "), int(input("Salary: ")))
    employees.append(emp)
    print("Added!")

def update():
    emp_id = int(input("ID to Update: "))
    for i, e in enumerate(employees):
        if e[0] == emp_id:
            employees[i] = (e[0], e[1], e[2], int(input("New Salary: ")))
            print("Updated!"); return
    print("Not Found!")

def delete():
    emp_id = int(input("ID to Delete: "))
    for e in employees:
        if e[0] == emp_id:
            employees.remove(e); print("Deleted!"); return
    print("Not Found!")

def show():
    for e in employees:
        print(e)

while True:
    print("\n1.Add  2.Update  3.Delete  4.Show  5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1: add()
    elif ch == 2: update()
    elif ch == 3: delete()
    elif ch == 4: show()
    elif ch == 5: break
    else: print("Invalid!")
