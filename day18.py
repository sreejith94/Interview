class BankAccount:

    # Constructor
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account Created Successfully")

    # Deposit function
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully")

    # Withdraw function
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn Successfully")
        else:
            print("Insufficient Balance")

    # Check Balance function
    def check_balance(self):
        print("Current Balance:", self.balance)

    # Destructor
    def __del__(self):
        print("Thank You for Banking")


# Main Program
name = input("Enter Account Holder Name: ")
balance = float(input("Enter Initial Balance: "))

account = BankAccount(name, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == 3:
        account.check_balance()

    elif choice == 4:
        del account
        break

    else:
        print("Invalid Choice")

class Patient:

    # Constructor
    def __init__(self, name, age, fee):
        self.name = name
        self.age = age
        self.fee = fee

    # Calculate Bill
    def calculate_bill(self):
        if self.age >= 60:
            bill = self.fee - (self.fee * 20 / 100)
            print("Senior Citizen Discount: 20%")
        else:
            bill = self.fee

        print("Final Bill: ₹", bill)

    # Display Patient Details
    def display_details(self):
        print("\nPatient Details")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Consultation Fee : ₹", self.fee)

    # Destructor
    def __del__(self):
        print("Patient record removed.")


# Main Program
name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
fee = float(input("Enter Consultation Fee: "))

p = Patient(name, age, fee)

p.display_details()
p.calculate_bill()

del p