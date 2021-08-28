"""Today I will be writing a program which allows the user to explore numerical operators using two numerical variables."""

__author__ = "730472595"

number_lh: str = input("Left-hand side: ")
number_rh: str = input("Right-hand side: ")

int_number_lh = int(number_lh)
int_number_rh = int(number_rh)

print(number_lh + " ** " + number_rh + " is " + str(int_number_lh ** int_number_rh))
print(number_lh + " / " + number_rh + " is " + str(int_number_lh / int_number_rh))
print(number_lh + " // " + number_rh + " is " + str(int_number_lh // int_number_rh))
print(number_lh + " % " + number_rh + " is " + str(int_number_lh % int_number_rh))