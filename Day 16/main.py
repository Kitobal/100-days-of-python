from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

the_menu = Menu()
the_coffe_maker = CoffeeMaker()
the_money_machine = MoneyMachine()

machine_on = True

while machine_on:
    choice = input(f"What do you want? {the_menu.get_items()}: ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        the_coffe_maker.report()
        the_money_machine.report()
    else:
        if the_menu.find_drink(choice):
            drink_choice = the_menu.find_drink(choice)
            if the_coffe_maker.is_resource_sufficient(drink_choice):
                if the_money_machine.make_payment(drink_choice.cost):
                    the_coffe_maker.make_coffee(drink_choice)
