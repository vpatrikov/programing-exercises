def ex_1():
    class Person():
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def talk(self):
            print(f"Hello, I am {self.name} and I am {self.age}")

    class Employee(Person):
        def __init__(self, name, age, employee_id):
            super().__init__(name, age)
            self.employee_id = employee_id

        def talk(self):
            print(f"Hello, I am {self.name} and I am {self.age}. My ID is {self.employee_id}")

    class Student(Person):
        def __init__(self, name, age, grade):
            super().__init__(name, age)
            self.grade = grade

        def talk(self):
            print(f"Hello! I am {self.name} and I am {self.age}. My grade at school is {self.grade}")

    person = None

    while True:
        data = input("Enter your name, age, and if you are a student or an employee (or none)\n").split(' ')
        if len(data) != 3 or not data[1].isdigit():
            print("\nInvalid Input")
        else:
            data[1] = int(data[1])
            break

    if data[2] == 'employee':
        emp_id = input("Enter your ID: ")
        person = Employee(data[0], data[1], emp_id)
    elif data[2] == 'student':
        while True:
            grade = input("Enter your grade: ")

            if grade.replace('.', '').isdigit():
                grade = round(float(grade), 2)
                person = Student(data[0], data[1], grade)
                break
            else:
                print("\nInvalid Input")
    else:
        person = Person(data[0], data[1])

    person.talk()

def ex_2():
    class BankAccount():
        def __init__(self, account_number, balance):
            self.account_number = account_number
            self.balance = balance
        
        def deposit(self, amount):
            self.balance += amount
        
        def withdraw (self, amount):
            self.balance -= amount

    class SavingsAccount(BankAccount):
        def __init__(self, account_number, balance, interest_rate, time):
            super().__init__(account_number, balance)
            self.interest_rate = interest_rate
            self.time = time

        def interestCalc(self):
            return self.balance*(1+ self.interest_rate*self.time)
        
    bankaccount = BankAccount(31481974897, 24)
    savingsacc = SavingsAccount(1231413, 431.2, 42.441, 5)

    while True:
        choice = input("\nWhat do you want to do?\n1. Deposit to bank account\n2. Withdraw from account\n3. Check interest of savings account\n")

        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                while True:
                    amount = input("\nEnter the amount you want to deposit: ")
                    if amount.isnumeric():
                        amount = round(float(amount), 2)
                        break
                    else:
                        print("\n\n\n\n\n\n\n\n\n\nInvalid Input")
                bankaccount.deposit(amount)
                print (f"\nNew balance is {bankaccount.balance}")
            elif choice == 2:
                while True:
                    amount = input("\nEnter the amount you want to withdraw: ")
                    if amount.isnumeric():
                        amount = round(float(amount), 2)
                        break
                    else:
                        print("\n\n\n\n\n\n\n\n\n\nInvalid Input")
                bankaccount.withdraw(amount)
                print (f"\nNew balance is {bankaccount.balance}")
            elif choice == 3:
                print(f"\nThe interest for your saving account is {round(savingsacc.interestCalc(), 2)}")

            break
        else:
            print("\n\n\n\n\n\nInvalid Input")


ex_1()    
            