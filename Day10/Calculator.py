#calculator

#print logo
from art import logo
print(logo)

#add
def add(n1,n2):
  return n1 + n2

#subtract
def subtract(n1,n2):
  return n1 - n2

#Multiply
def multiply(n1,n2):
  return n1* n2

#Divide
def divide(n1,n2):
  return n1 / n2

dictionary = {"+":add, "-":subtract, "*":multiply, "/":divide}

Continue_program = True
while Continue_program:
  for operator in dictionary:
    print(operator)
  operation_symbol= input("Type in the operation you want: ")
  perform_operation = dictionary[operation_symbol]
  result = perform_operation(n1 = float(input("Enter the first integer: ")), n2 = float(input("Enter the second integer: ")))
  print(f"The answer is: {round(result,2)}")
  user_decision = input("Do you still want to continue the calculator program? Type 'yes' or 'no'\n")
  if user_decision == 'no':
    Continue_program = False
