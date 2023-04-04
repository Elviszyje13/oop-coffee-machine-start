from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
atm = MoneyMachine()
menu = Menu()

items = menu.get_items()

while True:
    client_input = input(f"What would you like? {items}")

    if client_input == "off":
        break
    elif client_input == "report":
        cm.report()
        atm.report()
    else:
        order = menu.find_drink(client_input)

        if (order is not None) and (cm.is_resource_sufficient(order)):
            if atm.make_payment(order.cost):
                cm.make_coffee(order)







