# 11-3 employee: write a class called employee.
# the __init__() method should take in a first name, a last name, and
# an annual salary, and store each of these as attributes.
# write a method called give_raise() that adds $5,000 to the annual
# salary by default but also accepts a different raise amount.


class Employee:
    """collect first, last, salary from employee."""

    def __init__(self, first_name, last_name, salary):
        """store first, last, salary as attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary


    def give_raise(self, amount=5000):
        """add raise to salary"""
        self.salary += amount
    

    def show_info(self):
        """show the full name and salary of the employee"""
        print(f"{self.first_name.title()} {self.last_name.title()} - ${self.salary:,}")
        