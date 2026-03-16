# create an instance of the employee class
from employee import Employee

employees = []

# create a loop to continuously ask other employees
while True:
    print("\nEnter employee information")

    first = input("What is your first name? ").strip()
    last = input("What is your last name? ").strip()
    salary = int(input("What is your salary? "))

    emp = Employee(first, last, salary)
    employees.append(emp)

    give_raise = input("Would you like to give this employee a raise? (y/n): ").lower()
    if give_raise == "y":
        amount = input("Enter different amount or press 'Enter': ").strip()

        if amount:
            emp.give_raise(int(amount))
        else:
            emp.give_raise()

    add_another = input("Would you like to add another employee? (y/n): ").lower()
    if add_another != "y":
        break


print("\n----- Employee Summary -----")
for emp in employees:
    emp.show_info()
