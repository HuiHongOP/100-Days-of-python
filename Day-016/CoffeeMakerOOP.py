from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



def start_machine():
  coffee_type = Menu()
  coffee_maker = CoffeeMaker()
  money_machine = MoneyMachine()

  machine_on = True

  while machine_on:
    user_input = input(f"What would you like? {coffee_type.get_items()}: ")
    if user_input == "report":
      coffee_maker.report()
      money_machine.report()
    elif user_input =="off":
      machine_on = False
    else:
      user_coffee = coffee_type.find_drink(user_input)
      if coffee_maker.is_resource_sufficient(user_coffee) and money_machine.make_payment(user_coffee.cost):
        coffee_maker.make_coffee(user_coffee)
    
start_machine()
